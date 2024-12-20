import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def load_independent_data():
    return pd.read_csv('data/independent_data_with_features.csv')

def validate_model(model, data):
    X = data.drop('drug_response', axis=1)
    y = data['drug_response']
    
    predictions = model.predict(X)
    
    metrics = {
        'accuracy': accuracy_score(y, predictions),
        'precision': precision_score(y, predictions),
        'recall': recall_score(y, predictions),
        'f1_score': f1_score(y, predictions)
    }
    
    return metrics

if __name__ == "__main__":
    from model_training import train_models, load_data_with_features
    
    data = load_data_with_features()
    rf_model, svm_model, rf_metrics, svm_metrics = train_models(data)
    
    independent_data = load_independent_data()
    
    rf_validation_metrics = validate_model(rf_model, independent_data)
    svm_validation_metrics = validate_model(svm_model, independent_data)
    
    print("Random Forest Validation Metrics:", rf_validation_metrics)
    print("SVM Validation Metrics:", svm_validation_metrics)