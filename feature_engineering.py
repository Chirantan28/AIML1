import pandas as pd

def load_processed_data():
    return pd.read_csv('data/processed_data.csv')

def load_independent_processed_data():
    return pd.read_csv('data/independent_processed_data.csv')

def create_features(data):
    # Extract and create new features
    # Example feature engineering steps
    data['age_bmi_interaction'] = data['age'] * data['bmi']
    # Add more feature engineering steps as needed
    return data

if __name__ == "__main__":
    data = load_processed_data()
    data_with_features = create_features(data)
    data_with_features.to_csv('data/data_with_features.csv', index=False)
    
    independent_data = load_independent_processed_data()
    independent_data_with_features = create_features(independent_data)
    independent_data_with_features.to_csv('data/independent_data_with_features.csv', index=False)