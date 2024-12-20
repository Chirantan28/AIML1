import pandas as pd
import numpy as np

def load_data():
    # Load genomic, EHR, lab results, demographic data, and drug response
    genomic_data = pd.read_csv('data/genomic_data.csv')
    ehr_data = pd.read_csv('data/ehr_data.csv')
    lab_results = pd.read_csv('data/lab_results.csv')
    demographic_data = pd.read_csv('data/demographic_data.csv')
    drug_response = pd.read_csv('data/drug_response.csv')
    return genomic_data, ehr_data, lab_results, demographic_data, drug_response

def preprocess_data(genomic_data, ehr_data, lab_results, demographic_data, drug_response):
    # Clean and preprocess the data
    # Handle missing values, normalize, and standardize
    # Example preprocessing steps
    genomic_data.fillna(genomic_data.mean(), inplace=True)
    ehr_data.fillna(ehr_data.mean(), inplace=True)
    lab_results.fillna(lab_results.mean(), inplace=True)
    
    # Convert categorical data to numerical (e.g., gender)
    demographic_data['gender'] = demographic_data['gender'].map({'Male': 0, 'Female': 1})
    
    # Fill missing values for demographic data after converting categorical data
    demographic_data.fillna(demographic_data.mean(), inplace=True)
    
    # Merge data
    merged_data = pd.merge(genomic_data, ehr_data, on='patient_id')
    merged_data = pd.merge(merged_data, lab_results, on='patient_id')
    merged_data = pd.merge(merged_data, demographic_data, on='patient_id')
    merged_data = pd.merge(merged_data, drug_response, on='patient_id')
    
    return merged_data

def preprocess_independent_data():
    # Load independent data
    independent_genomic_data = pd.read_csv('data/independent_genomic_data.csv')
    independent_ehr_data = pd.read_csv('data/independent_ehr_data.csv')
    independent_lab_results = pd.read_csv('data/independent_lab_results.csv')
    independent_demographic_data = pd.read_csv('data/independent_demographic_data.csv')
    independent_drug_response = pd.read_csv('data/independent_drug_response.csv')
    
    # Preprocess independent data
    return preprocess_data(independent_genomic_data, independent_ehr_data, independent_lab_results, independent_demographic_data, independent_drug_response)

if __name__ == "__main__":
    genomic_data, ehr_data, lab_results, demographic_data, drug_response = load_data()
    processed_data = preprocess_data(genomic_data, ehr_data, lab_results, demographic_data, drug_response)
    processed_data.to_csv('data/processed_data.csv', index=False)
    
    independent_processed_data = preprocess_independent_data()
    independent_processed_data.to_csv('data/independent_processed_data.csv', index=False)