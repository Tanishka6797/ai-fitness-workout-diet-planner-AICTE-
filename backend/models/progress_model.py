from sklearn.linear_model import LinearRegression
import numpy as np

model = LinearRegression()

def train_model(weights, weeks):
    X = np.array(weeks).reshape(-1, 1)
    y = np.array(weights)
    model.fit(X, y)
    return model

def predict_weight(week):
    return model.predict([[week]])[0]