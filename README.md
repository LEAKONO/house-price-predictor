# 🏡 House Price Predictor

A simple machine learning project using Python to predict house prices based on size and number of bedrooms.

## 🚀 Features

- Trains a Linear Regression model
- Predicts house price for given input
- Visualizes original data and predicted result
- Clean folder structure for modular development

## 🧠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Joblib

## 📁 Folder Structure

```plaintext
house-price-predictor/
├── model.py           # Train and save the model
├── predict.py         # Predict house price using trained model
├── visualize.py       # Plot the results
├── requirements.txt   # Project dependencies
├── README.md          # Project info
└── .gitignore         # Files to ignore




## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/LEAKONO/house-price-predictor
cd house-price-predictor
```
### Create virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### Install dependencies:

```
pip install -r requirements.txt
```
## Usage
Train the model:

```
python3 model.py
```
Predict for a new house:

```
python3 predict.py
```
Visualize the results:

```
python3 visualize.py
```
## Contributing
Contributions are welcome. Please fork the repo and create a pull request!