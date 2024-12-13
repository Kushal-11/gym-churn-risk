# README.md

# Gym Churn Risk Prediction

This project aims to predict churn risk for gym members using machine learning techniques. It utilizes user data, subscription plans, and gym location information to assess the likelihood of members discontinuing their gym memberships.

## Project Structure

- **data/**: Contains CSV files with user information, subscription plans, check-in/check-out history, and gym locations.
  - `USERS_DATA.CSV`: User information including demographics and subscription details.
  - `SUBSCRIPTION_PLANS.CSV`: Details of subscription plans available at the gym.
  - `CHECKIN_CHECKOUT_HISTORY_UPDATED.CSV`: Intended for check-in and check-out history (currently empty).
  - `GYM_LOCATIONS_DATA.CSV`: Information about gym locations and their facilities.

- **models/**: Contains the trained machine learning model for predicting churn risk.
  - `churn_model.pkl`: The serialized model file.

- **notebooks/**: Jupyter notebooks for data preprocessing and exploratory data analysis.
  - `data_preprocessing.ipynb`: Notebook for data cleaning and feature engineering.

- **src/**: Source code for data processing, model training, and dashboard setup.
  - `__init__.py`: Marks the directory as a Python package.
  - `data_preprocessing.py`: Functions for loading and cleaning data.
  - `train_model.py`: Logic for training the machine learning model.
  - `dashboard.py`: Streamlit dashboard for displaying churn risk predictions.

- **requirements.txt**: Lists the dependencies required for the project.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd gym-churn-risk
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit dashboard:
   ```
   streamlit run src/dashboard.py
   ```

## Usage

- The dashboard will display churn risk predictions based on user data and other relevant features.
- Users can interact with the dashboard to visualize data and understand churn risk factors.

## License

This project is licensed under the MIT License.