import pandas as pd
import joblib

model = joblib.load("house_model.pkl")

new_house_df = pd.DataFrame([[2200, 3]], columns=["Size", "Bedrooms"])
predicted_price = model.predict(new_house_df)

print(f"Predicted price for 2200 sqft and 3 bedrooms: ${predicted_price[0]:,.2f}")
