import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

data = pd.read_csv("economic_data.csv")

# Préparation des données pour le modèle
data["Month"] = pd.to_datetime(data["Date"]).dt.month
X = data[["Month"]]
y = data["Exchange_Rate"]

# Division des données
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement du modèle
model = RandomForestRegressor()
model.fit(X_train, y_train)
