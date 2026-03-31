import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except:
        return None

def preprocess_data(data):
    data = data.fillna(data.mean(numeric_only=True))
    X = data[['area', 'bedrooms', 'bathrooms', 'location_distance', 'furnishing']]
    y = data['price']
    return X, y

def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def save_model(model, filename="model.pkl"):
    pickle.dump(model, open(filename, "wb"))

def load_model(filename="model.pkl"):
    try:
        model = pickle.load(open(filename, "rb"))
        return model
    except:
        return None

def predict_price(model):
    try:
        area = float(input("Area (sq ft): "))
        bedrooms = int(input("Bedrooms: "))
        bathrooms = int(input("Bathrooms: "))
        distance = float(input("Distance from college (km): "))
        furnishing = int(input("Furnishing (1 = Yes, 0 = No): "))

        features = pd.DataFrame([[area, bedrooms, bathrooms, distance, furnishing]],
                                columns=['area', 'bedrooms', 'bathrooms', 'location_distance', 'furnishing'])

        prediction = model.predict(features)

        print(f"Estimated Rent: ₹ {int(prediction[0])}")
    except:
        print("Invalid input")

if __name__ == "__main__":
    data = load_data("data.csv")

    if data is not None:
        X, y = preprocess_data(data)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = train_model(X_train, y_train)

        save_model(model)

        loaded_model = load_model()

        if loaded_model:
            predict_price(loaded_model)