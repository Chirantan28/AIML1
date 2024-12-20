import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def load_data_with_features():
    return pd.read_csv('data/data_with_features.csv')

def train_models(data):
    X = data.drop('drug_response', axis=1)
    y = data['drug_response']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train Random Forest model
    rf_model = RandomForestClassifier()
    rf_model.fit(X_train, y_train)
    rf_predictions = rf_model.predict(X_test)
    
    # Train SVM model
    svm_model = SVC()
    svm_model.fit(X_train, y_train)
    svm_predictions = svm_model.predict(X_test)
    
    # Evaluate models
    rf_metrics = {
        'accuracy': accuracy_score(y_test, rf_predictions),
        'precision': precision_score(y_test, rf_predictions),
        'recall': recall_score(y_test, rf_predictions),
        'f1_score': f1_score(y_test, rf_predictions)
    }
    
    svm_metrics = {
        'accuracy': accuracy_score(y_test, svm_predictions),
        'precision': precision_score(y_test, svm_predictions),
        'recall': recall_score(y_test, svm_predictions),
        'f1_score': f1_score(y_test, svm_predictions)
    }
    
    return rf_model, svm_model, rf_metrics, svm_metrics

if __name__ == "__main__":
    data = load_data_with_features()
    rf_model, svm_model, rf_metrics, svm_metrics = train_models(data)
    print("Random Forest Metrics:", rf_metrics)
    print("SVM Metrics:", svm_metrics)