import pandas as pd

def load_user_data(file_path):
    """Load user data from CSV file."""
    return pd.read_csv(file_path)

def load_subscription_data(file_path):
    """Load subscription plan data from CSV file."""
    return pd.read_csv(file_path)

def load_gym_locations_data(file_path):
    """Load gym locations data from CSV file."""
    return pd.read_csv(file_path)

def preprocess_user_data(user_data):
    """Preprocess user data for modeling."""
    # Example preprocessing steps
    user_data['age'] = pd.to_datetime('today').year - pd.to_datetime(user_data['birthdate']).dt.year
    user_data['sign_up_date'] = pd.to_datetime(user_data['sign_up_date'])
    user_data['churn_risk'] = user_data['subscription_plan'].apply(lambda x: 1 if x == 'Basic' else 0)  # Example churn risk logic
    return user_data

def preprocess_subscription_data(subscription_data):
    """Preprocess subscription plan data."""
    # Example preprocessing steps
    return subscription_data

def preprocess_gym_locations_data(gym_locations_data):
    """Preprocess gym locations data."""
    # Example preprocessing steps
    return gym_locations_data

def main():
    user_data = load_user_data('../data/USERS_DATA.CSV')
    subscription_data = load_subscription_data('../data/SUBSCRIPTION_PLANS.CSV')
    gym_locations_data = load_gym_locations_data('../data/GYM_LOCATIONS_DATA.CSV')

    user_data = preprocess_user_data(user_data)
    subscription_data = preprocess_subscription_data(subscription_data)
    gym_locations_data = preprocess_gym_locations_data(gym_locations_data)

    # Save preprocessed data if needed
    user_data.to_csv('../data/preprocessed_user_data.csv', index=False)

if __name__ == "__main__":
    main()