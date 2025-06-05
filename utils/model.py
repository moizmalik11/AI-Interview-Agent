import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
from sklearn.preprocessing import LabelEncoder

def train_cheating_detection_model(csv_file_path):
    df = pd.read_csv(csv_file_path)

    for column in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])

    X = df.drop(columns=['label'])
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)

    model_filename = 'data/models/cheating_detector_model.pkl'
    joblib.dump(model, model_filename)

    model_columns_filename = 'data/models/cheating_scaler.pkl'
    joblib.dump(X.columns.tolist(), model_columns_filename)

    return report, model_filename

csv_file_path = "data/datasets/advanced_features.csv"
report, model_filename = train_cheating_detection_model(csv_file_path)
print("Model Evaluation Report:\n", report)
print("Model saved as:", model_filename)


def make_prediction(input_data):
    input_df = pd.DataFrame([input_data]) 
    model = joblib.load('data/models/cheating_detector_model.pkl')
    model_columns = joblib.load('data/models/cheating_scaler.pkl')
    missing_cols = set(model_columns) - set(input_df.columns)
    for col in missing_cols:
        input_df[col] = 0  

    input_df = input_df[model_columns]

    for column in input_df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        input_df[column] = le.fit_transform(input_df[column])

    predictions = model.predict(input_df)

    return predictions
