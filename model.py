import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = {
    "Size": [1000, 1500, 2000, 2500, 3000],
    "Bedrooms": [2, 3, 3, 4, 4],
    "Price": [300000, 400000, 500000, 600000, 75000]
}

df = pd.DataFrame(data)
X = df[["Size", "Bedrooms"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

print("Model coefficients:", model.coef_)
print("Model intercept:", model.intercept_)

joblib.dump(model, "house_model.pkl")
