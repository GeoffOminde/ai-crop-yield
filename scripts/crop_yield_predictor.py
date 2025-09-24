import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------
# Setup folders
# ------------------------------------------------
DATA_PATH = "data/crop_yield.csv"   # adjust if filename differs
RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

# -----------------------------
# 1. Load Dataset
# -----------------------------
data = pd.read_csv(DATA_PATH)

# -----------------------------
# 2. Reshape into long format
# -----------------------------
long_data = pd.DataFrame({
    "Crop": ["Rice"] * len(data) + ["Wheat"] * len(data) + ["Sugarcane"] * len(data) + ["Cotton"] * len(data),
    "Area": pd.concat([
        data["RICE AREA (1000 ha)"],
        data["WHEAT AREA (1000 ha)"],
        data["SUGARCANE AREA (1000 ha)"],
        data["COTTON AREA (1000 ha)"]
    ], ignore_index=True),
    "Production": pd.concat([
        data["RICE PRODUCTION (1000 tons)"],
        data["WHEAT PRODUCTION (1000 tons)"],
        data["SUGARCANE PRODUCTION (1000 tons)"],
        data["COTTON PRODUCTION (1000 tons)"]
    ], ignore_index=True),
    "Yield": pd.concat([
        data["RICE YIELD (Kg per ha)"],
        data["WHEAT YIELD (Kg per ha)"],
        data["SUGARCANE YIELD (Kg per ha)"],
        data["COTTON YIELD (Kg per ha)"]
    ], ignore_index=True)
})

print("\nRestructured Long Format:")
print(long_data.head())

# Save restructured dataset
long_data.to_csv(os.path.join(RESULTS_DIR, "long_format_data.csv"), index=False)

# -----------------------------
# 3. Define features & target
# -----------------------------
X = long_data[["Crop", "Area", "Production"]]
y = long_data["Yield"]

# -----------------------------
# 4. Encode categorical + Model pipeline
# -----------------------------
categorical_features = ["Crop"]
numeric_features = ["Area", "Production"]

# OneHotEncode 'Crop'
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(), categorical_features),
        ("num", "passthrough", numeric_features)
    ]
)

# Full pipeline: preprocess + regression
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# -----------------------------
# 5. Train/Test Split & Train
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)

# -----------------------------
# 6. Evaluate
# -----------------------------
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n📈 Generalized Multi-Crop Model Performance:")
print(f" - Mean Squared Error: {mse:.2f}")
print(f" - R² Score: {r2:.2f}")

# -----------------------------
# 7. Example Predictions
# -----------------------------
example = pd.DataFrame({
    "Crop": ["Rice", "Wheat", "Sugarcane", "Cotton"],
    "Area": [600, 50, 10, 5],
    "Production": [350, 25, 200, 1]
})

predictions = model.predict(example)
example["Predicted Yield (Kg/ha)"] = predictions

print("\n🌾 Example Predictions:")
print(example)
