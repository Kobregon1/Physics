from mp_api.client import MPRester as Mpr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor
from xgboost import XGBRFRegressor
from sklearn.ensemble import RandomForestRegressor

m = Mpr("************************")  # Include your own Materials Project API Key here

# Can search up anonymous materials, as an example, of the form 'ABC03'
# We want information regarding band_gap, formula name, and structure (a.k.a CIF file)
results = m.summary.search(formula=['ABC03'], fields=["band_gap", "formula_pretty", "structure"])

mean_atomic_numbers = []
max_atomic_numbers = []
min_atomic_numbers = []
std_atomic_numbers = []

# Lattice parameters
a_parameters = []
b_parameters = []
c_parameters = []
alpha_parameters = []
beta_parameters = []
gamma_parameters = []

# Inter-atomic distances:
mean_distance_matrix = []
max_distance_matrix = []
min_distance_matrix = []
std_distance_matrix = []

# Collect the target value a.k.a band gaps
band_gaps = []

for r in results:
    structure = r.structure
    bg = r.band_gap

    mean_atomic_numbers += [np.mean(structure.atomic_numbers)]
    max_atomic_numbers += [np.max(structure.atomic_numbers)]
    min_atomic_numbers += [np.min(structure.atomic_numbers)]
    std_atomic_numbers += [np.std(structure.atomic_numbers)]

    # Lattice parameters:
    a_parameters += [structure.lattice.abc[0]]
    b_parameters += [structure.lattice.abc[1]]
    c_parameters += [structure.lattice.abc[2]]
    alpha_parameters += [structure.lattice.angles[0]]
    beta_parameters += [structure.lattice.angles[1]]
    gamma_parameters += [structure.lattice.angles[2]]

    mean_distance_matrix += [np.mean(structure.distance_matrix)]
    max_distance_matrix += [np.max(structure.distance_matrix)]
    min_distance_matrix += [np.min(structure.distance_matrix)]
    std_distance_matrix += [np.std(structure.distance_matrix)]

    band_gaps += [bg]

plt.rcParams.update({'font.size': 20})

# Histogram of how many structures with these band gap values
plt.figure(figsize=(10, 10))
plt.hist(band_gaps, bins=100)
plt.xlabel('Band Gap Ranges [eV]')
plt.ylabel('# of structures with Band Gap value')
plt.savefig('Histogram_PDF.pdf', bbox_inches='tight')

# Scatter plot of the range of structures with these band gap values
band_gaps_sorted = sorted(band_gaps)

plt.figure(figsize=(10, 10))
plt.plot(band_gaps_sorted)
plt.xlabel('Total # of structures')
plt.ylabel('Band Gap Ranges [eV]')
plt.savefig('ScatterPlot.pdf', bbox_inches='tight')


dataset_df = pd.DataFrame({"mean_atomic_numbers": mean_atomic_numbers,
                           "max_atomic_numbers": max_atomic_numbers,
                           "min_atomic_numbers": min_atomic_numbers,
                           "std_atomic_numbers": std_atomic_numbers,
                           "a_parameters": a_parameters,
                           "b_parameters": b_parameters,
                           "c_parameters": c_parameters,
                           "alpha_parameters": alpha_parameters,
                           "beta_parameters": beta_parameters,
                           "gamma_parameters": gamma_parameters,
                           "mean_distance_matrix": mean_distance_matrix,
                           "max_distance_matrix": max_distance_matrix,
                           "min_distance_matrix": min_distance_matrix,
                           "std_distance_matrix": std_distance_matrix
                           })

scaler = StandardScaler().fit(dataset_df)
scaled_dataset_df = scaler.transform(dataset_df)


X_train_scaled, X_test_scaled, y_train, y_test = train_test_split(
    scaled_dataset_df, band_gaps, test_size=.2, random_state=None)

# Comparing 3 ML models: XGBoost Regressor, XGBoost Random Forest Regressor, & Random Forest Regressor

# XGBoost Regressor
regr_xg = XGBRegressor(objective='reg:squarederror', colsample_bytree=0.5, learning_rate=0.1,
                       max_depth=500, alpha=10, n_estimators=500)
regr_xg.fit(X_train_scaled, y_train)
y_predicted = regr_xg.predict(X_test_scaled)

print('XGBOOST MSE = \t'+str(mean_squared_error(y_test, y_predicted))+'\n')
print('XGBOOST R2 = \t'+str(r2_score(y_test, y_predicted))+'\n')
print('-----------')

# XGBoost predicted BG vs Original Values of BG via DFT from the MP database
xPlot = y_test
yPlot = y_predicted
plt.figure(figsize=(10, 10))
plt.plot(xPlot, yPlot, 'ro')
plt.plot(xPlot, xPlot)
plt.ylabel('XGBOOST')
plt.xlabel('DFT')
plt.savefig('XGBoost_Correlation_Test.pdf', bbox_inches='tight')

# XGBoost Random Forest Regressor
regr_xgrf = XGBRFRegressor(objective='reg:squarederror', colsample_bytree=0.5,
                           max_depth=500, alpha=10, n_estimators=500)
regr_xgrf.fit(X_train_scaled, y_train)
y_predicted = regr_xgrf.predict(X_test_scaled)

print('XGBOOSTRF MSE =\t'+str(mean_squared_error(y_test, y_predicted))+'\n')
print('XGBOOSTRF R2 =\t'+str(r2_score(y_test, y_predicted))+'\n')
print('-------------')

# XGBoostRF predicted BG vs Original Values of BG via DFT from the MP database
xPlot = y_test
yPlot = y_predicted
plt.figure(figsize=(10, 10))
plt.plot(xPlot, yPlot, 'ro')
plt.plot(xPlot, xPlot)
plt.ylabel('XGBOOSTRF')
plt.xlabel('DFT')
plt.savefig('XGBOOSTRF_Correlation_Test.pdf', bbox_inches='tight')

# Random Forest Regressor
regr = RandomForestRegressor(n_estimators=500, max_depth=500, random_state=1)
regr.fit(X_train_scaled, y_train)
y_predicted = regr.predict(X_test_scaled)

print('RF MSE =\t'+str(mean_squared_error(y_test, y_predicted))+'\n')
print('RF R2 =\t'+str(r2_score(y_test, y_predicted))+'\n')

# Random Forest predicted BG vs Original Values of BG via DFT from the MP database
xPlot = y_test
yPlot = y_predicted
plt.figure(figsize=(10, 10))
plt.plot(xPlot, yPlot, 'ro')
plt.plot(xPlot, xPlot)
plt.ylabel('RF')
plt.xlabel('DFT')
plt.savefig('RF_Correlation_Test.pdf', bbox_inches='tight')
