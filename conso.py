# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 16:34:58 2025
@author: jules
"""

import datetime
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
from sklearn.preprocessing import StandardScaler

# --- 1. CHARGEMENT ET PRÉPARATION DE BASE ---
data = np.genfromtxt('conso_campus_aix.csv', delimiter=',', skip_header=1)
conso = data[:, 8]
y_orig = conso 

Jours_du_mois = data[:, 0].astype(int)
Mois_orig = data[:, 1].astype(int)
Annees_orig = data[:, 2].astype(int)
Heure_orig = data[:, 3].astype(int)

# --- 2. ENCODAGES CYCLIQUES ET VARIABLES TEMPORELLES ---
H_sin = np.sin(2 * np.pi * Heure_orig / 24)
H_cos = np.cos(2 * np.pi * Heure_orig / 24)
M_sin = np.sin(2 * np.pi * Mois_orig / 12)
M_cos = np.cos(2 * np.pi * Mois_orig / 12)

jours_de_la_semaine = []
for annee, mois, jour in zip(Annees_orig, Mois_orig, Jours_du_mois):
    date_obj = datetime.date(annee, mois, jour)
    jours_de_la_semaine.append(date_obj.weekday())
jours_de_la_semaine = np.array(jours_de_la_semaine)

S_sin = np.sin(2 * np.pi * jours_de_la_semaine / 7)
S_cos = np.cos(2 * np.pi * jours_de_la_semaine / 7)

# Variable binaire Week-end
is_weekend = (jours_de_la_semaine >= 5).astype(int)

# [AJOUT] Variable Activé/Veille (ex: 1 si entre 7h et 20h, 0 sinon)
# Cette variable aide le modèle à mieux caler le "talon" de consommation nocturne
is_active_hours = ((Heure_orig >= 7) & (Heure_orig <= 20)).astype(int)

# --- 3. FEATURE ENGINEERING AVANCÉ ---
variables_meteo = data[:, [4, 5, 6, 7]]
lag_1 = np.roll(y_orig, 1)
lag_2 = np.roll(y_orig, 2)
lag_24 = np.roll(y_orig, 24)
lag_168 = np.roll(y_orig, 168)
diff_1h = lag_1 - lag_2
diff_24h = lag_1 - lag_24

# --- 4. CONSTRUCTION DE LA MATRICE X ET Y ---
X_full = np.column_stack((
    variables_meteo, 
    M_sin, M_cos, 
    H_sin, H_cos, 
    S_sin, S_cos, 
    is_weekend,
    is_active_hours, # Ajout de la variable d'activité
    lag_1, lag_24, lag_168, 
    diff_1h, diff_24h
))

X = X_full[168:]
y = y_orig[168:]

# Transformation Logarithmique
y_log = np.log1p(y)

# --- 5. SPLIT SÉQUENTIEL ---
test_size = 0.2
split_index = int(len(X) * (1 - test_size))

X_train, X_test = X[:split_index], X[split_index:]
y_train_log, y_test_log = y_log[:split_index], y_log[split_index:]
y_test_real = y[split_index:] 

# --- 6. MISE À L'ÉCHELLE ---
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --- 7. MODÈLE MLP ---
mlp = MLPRegressor(
    hidden_layer_sizes=(100, 100, 50),
    activation='relu',
    solver='adam',
    max_iter=2000,
    early_stopping=True,
    n_iter_no_change=20,
    alpha=0.5)

mlp.fit(X_train_scaled, y_train_log)

# --- 8. ÉVALUATION ET INVERSION ---
y_pred_test_log = mlp.predict(X_test_scaled)
y_pred_test = np.expm1(y_pred_test_log)

# Calcul des métriques demandées
rmse_test = np.sqrt(mean_squared_error(y_test_real, y_pred_test))
mae_test = mean_absolute_error(y_test_real, y_pred_test)
mape_test = mean_absolute_percentage_error(y_test_real, y_pred_test) * 100

print(f"--- RÉSULTATS FINAUX ---")
print(f"RMSE Test : {rmse_test:.2f}")
print(f"MAE Test  : {mae_test:.2f} (Erreur moyenne absolue)")
print(f"MAPE Test : {mape_test:.2f} % (Erreur moyenne en pourcentage)")

# --- 9. VISUALISATION ---
plt.figure(figsize=(12, 6))
plt.plot(y_test_real[-200:], label="Réel", color='black', alpha=0.6)
plt.plot(y_pred_test[-200:], label=f"Prédiction (MAPE: {mape_test:.2f}%)", color='red', linestyle='--')
plt.title('Zoom 200h : Modèle avec variables Week-end, Activité et Log-Transform')
plt.xlabel('Heures')
plt.ylabel('Consommation')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Scatter Plot
plt.figure(figsize=(7, 7))
plt.scatter(y_test_real, y_pred_test, alpha=0.5, color='blue')
plt.plot([y_test_real.min(), y_test_real.max()], [y_test_real.min(), y_test_real.max()], 'r--', lw=2)
plt.xlabel('Valeurs Réelles')
plt.ylabel('Valeurs Prédites')
plt.title(f'Corrélation (MAPE : {mape_test:.2f}%)')
plt.show()