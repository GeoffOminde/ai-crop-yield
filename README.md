# 🌾 AI for Zero Hunger: Multi-Crop Yield Prediction (SDG 2)

This project applies **Machine Learning** to support **UN Sustainable Development Goal 2 (Zero Hunger)** by predicting crop yields across multiple crops (Rice, Wheat, Sugarcane, Cotton).  
The goal is to help farmers, policymakers, and researchers improve agricultural planning, reduce waste, and enhance food security.

---

## 🚀 Overview
- **Problem:** Farmers face unpredictable harvests due to climate change, soil degradation, and poor resource planning.  
- **Solution:** A generalized **ML model** that predicts yields for multiple crops using area and production data, with `Crop` treated as a categorical feature.  
- **Approach:** Supervised Learning (Regression).  
- **Algorithms:** Linear Regression (baseline), Random Forest (extension).  
- **Dataset:** Open agriculture datasets (e.g., FAO/India agriculture). A sample CSV is provided.  

---

## 📂 Repository Structure

ai-crop-yield/
│── data/
│ └── crop_yield.csv # Raw dataset
│
│── notebooks/
│ └── crop_yield_analysis.ipynb # Jupyter Notebook (exploration + training)
│
│── scripts/
│ └── crop_yield_analysis.py # Python script for training
│
│── results/
│ ├── long_format_data.csv # Restructured dataset
│ 
│ 
│ 
│
│── README.md # Documentation
│── REPORT.md # 1-page project summary
│── PITCH_DECK.pdf # Pitch slides for stakeholders
│── requirements.txt # Dependencies


---

## ⚙️ Setup & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-crop-yield.git
cd ai-crop-yield
```
## 2. Create Virtual Environment & Install Dependencies
```bash
python -m venv .venv
source .venv/bin/activate   # (Linux/Mac)
.venv\Scripts\activate      # (Windows)

pip install -r requirements.txt
```
## 3. Run the Model
Option 1: Jupyter Notebook

```bash
jupyter notebook notebooks/crop_yield_analysis.ipynb
```
Option 2: Python Script

```bash
python scripts/train_model.py
```
This will:
Load and reshape the dataset into long format (`Crop`, `Area`, `Production`, `Yield`)/
Train regression models/
Evaluate results (MSE, R²)/
Save outputs in `results`/

## 📊 Example Results
Sample Metrics
(Using Linear Regression on sample dataset)
MSE: 45.2
R²: 0.89

(Random Forest generally improves performance.)
Example Predictions
Input:
Crop	Area	Production
Rice	600	350
Wheat	50	25
Sugarcane	10	200
Cotton	5	1

Output:
Crop	Predicted Yield (Kg/ha)
Rice	590.3
Wheat	520.1
Sugarcane	2010.7
Cotton	410.2

## 🌍 Ethical Reflection
Bias Risk: If dataset excludes rural smallholder farms, predictions may skew toward industrial farming./
Fairness: Ensure equal benefit across regions and crop types./
Sustainability: Better yield forecasting reduces waste, strengthens food systems, and supports SDG 2./

## 📢 Citation
“AI can be the bridge between innovation and sustainability.” — UN Tech Envoy

## ✅ Next Steps
Integrate weather, soil, and fertilizer features for richer predictions./
Experiment with advanced models (XGBoost, Neural Networks)./
Deploy as an API (Flask/FastAPI) for real-world integration./
Build a farmer-friendly dashboard with data visualizations./

---
