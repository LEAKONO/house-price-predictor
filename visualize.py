import pandas as pd
import joblib
import matplotlib.pyplot as plt

data = {
    "Size": [1000, 1500, 2000, 2500, 3000],
    "Bedrooms": [2, 3, 3, 4, 4],
    "Price": [300000, 400000, 500000, 600000, 650000]
}
df = pd.DataFrame(data)

model = joblib.load("house_model.pkl")
new_house = pd.DataFrame([[2200, 3]], columns=["Size", "Bedrooms"])
predicted_price = model.predict(new_house)

plt.scatter(df["Size"], df["Price"], color='blue', label='Original Data')
plt.scatter(2200, predicted_price[0], color='red', label='Predicted Price')

plt.xlabel("Size (sqft)")
plt.ylabel("Price ($)")
plt.title("House Price Prediction")
plt.legend()
plt.grid(True)
plt.savefig("prediction_plot.png")
