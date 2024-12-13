import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def load_data():
    users_data = pd.read_csv('../data/USERS_DATA.CSV')
    subscription_data = pd.read_csv('../data/SUBSCRIPTION_PLANS.CSV')
    # Assuming check-in/check-out data will be used in the future
    # checkin_data = pd.read_csv('../data/CHECKIN_CHECKOUT_HISTORY_UPDATED.CSV')
    # gym_locations_data = pd.read_csv('../data/GYM_LOCATIONS_DATA.CSV')
    
    return users_data, subscription_data

def preprocess_data(users_data, subscription_data):
    # Merge users data with subscription data
    data = users_data.merge(subscription_data, on='subscription_plan', how='left')
    
    # Convert categorical variables to numerical
    data['gender'] = data['gender'].map({'Male': 0, 'Female': 1, 'Non-binary': 2})
    data['subscription_plan'] = data['subscription_plan'].map({'Basic': 0, 'Pro': 1, 'Student': 2})
    
    # Drop unnecessary columns
    data = data.drop(columns=['user_id', 'first_name', 'last_name', 'birthdate', 'sign_up_date', 'user_location'])
    
    return data

def train_model(data):
    X = data.drop('subscription_plan', axis=1)
    y = data['subscription_plan']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    # Save the model
    joblib.dump(model, '../models/churn_model.pkl')

if __name__ == "__main__":
    users_data, subscription_data = load_data()
    processed_data = preprocess_data(users_data, subscription_data)
    train_model(processed_data)