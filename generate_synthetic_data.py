import pandas as pd
import numpy as np

def generate_genomic_data(num_samples):
    np.random.seed(42)
    data = {
        'patient_id': range(1, num_samples + 1),
        'gene1': np.random.rand(num_samples),
        'gene2': np.random.rand(num_samples),
        'gene3': np.random.rand(num_samples)
    }
    return pd.DataFrame(data)

def generate_ehr_data(num_samples):
    np.random.seed(42)
    data = {
        'patient_id': range(1, num_samples + 1),
        'condition1': np.random.randint(0, 2, num_samples),
        'condition2': np.random.randint(0, 2, num_samples),
        'condition3': np.random.randint(0, 2, num_samples)
    }
    return pd.DataFrame(data)

def generate_lab_results(num_samples):
    np.random.seed(42)
    data = {
        'patient_id': range(1, num_samples + 1),
        'lab1': np.random.rand(num_samples),
        'lab2': np.random.rand(num_samples),
        'lab3': np.random.rand(num_samples)
    }
    return pd.DataFrame(data)

def generate_demographic_data(num_samples):
    np.random.seed(42)
    data = {
        'patient_id': range(1, num_samples + 1),
        'age': np.random.randint(20, 80, num_samples),
        'gender': np.random.choice(['Male', 'Female'], num_samples),
        'bmi': np.random.rand(num_samples) * 10 + 20
    }
    return pd.DataFrame(data)

def generate_drug_response(num_samples):
    np.random.seed(42)
    data = {
        'patient_id': range(1, num_samples + 1),
        'drug_response': np.random.randint(0, 2, num_samples)
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    num_samples = 1000
    
    genomic_data = generate_genomic_data(num_samples)
    ehr_data = generate_ehr_data(num_samples)
    lab_results = generate_lab_results(num_samples)
    demographic_data = generate_demographic_data(num_samples)
    drug_response = generate_drug_response(num_samples)
    
    genomic_data.to_csv('data/genomic_data.csv', index=False)
    ehr_data.to_csv('data/ehr_data.csv', index=False)
    lab_results.to_csv('data/lab_results.csv', index=False)
    demographic_data.to_csv('data/demographic_data.csv', index=False)
    drug_response.to_csv('data/drug_response.csv', index=False)
    
    # Generate independent data
    num_independent_samples = 200
    
    independent_genomic_data = generate_genomic_data(num_independent_samples)
    independent_ehr_data = generate_ehr_data(num_independent_samples)
    independent_lab_results = generate_lab_results(num_independent_samples)
    independent_demographic_data = generate_demographic_data(num_independent_samples)
    independent_drug_response = generate_drug_response(num_independent_samples)
    
    independent_genomic_data.to_csv('data/independent_genomic_data.csv', index=False)
    independent_ehr_data.to_csv('data/independent_ehr_data.csv', index=False)
    independent_lab_results.to_csv('data/independent_lab_results.csv', index=False)
    independent_demographic_data.to_csv('data/independent_demographic_data.csv', index=False)
    independent_drug_response.to_csv('data/independent_drug_response.csv', index=False)