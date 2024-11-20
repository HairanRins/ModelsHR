import pandas as pd
import numpy as np

# Génération de données simulées
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", end="2024-01-01", freq="M")
exchange_rates = np.random.uniform(3.5, 5.0, len(dates))  # Taux de change aléatoire
data = pd.DataFrame({"Date": dates, "Exchange_Rate": exchange_rates})

# Exporter les données vers un fichier CSV
data.to_csv("economic_data.csv", index=False)
print("Les données simulées ont été générées et enregistrées dans 'economic_data.csv'.")
