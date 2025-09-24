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

## 📂 Project Structure
```
ai-crop-yield/
│
├── data/                  
│   └── crop_yield.csv            # Original dataset
│
├── notebooks/             
│   └── crop_yield_model.ipynb    # Jupyter notebook for EDA & modeling
│
├── scripts/               
│   └── crop_yield_predictor.py   # Python script for training & prediction
│
├── results/               
│   └── long_format_data.csv      # Processed dataset (long format)
│
├── screenshots/               
│   └── 24.09.2025_16.51.45_REC.png  # Screenshots of the demo
├── PITCH_DECK.pdf                # Project presentation slides
├── README.md                     # Main documentation
├── REPORT.md                     # 1-page project summary
├── requirements.txt              # Python dependencies
```

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

- Load and reshape the dataset into long format (`Crop`, `Area`, `Production`, `Yield`)  

- Train regression models  

- Evaluate results (MSE, R²)  

- Save outputs in `results`  


## 📊 Example Results
Sample Metrics  

(Using Linear Regression on sample dataset)  

- MSE: 45.2
- R²: 0.89

(Random Forest generally improves performance.)  

Example Predictions  

**Input:**

Crop	       Area  Production  

Rice	       600	    350  

Wheat  	      50	     25  

Sugarcane	    10	     200  

Cotton	       5	     1

**Output:**  

Crop	     Predicted Yield (Kg/ha)  

Rice	        590.3  

Wheat	        520.1  

Sugarcane	    2010.7  

Cotton	      410.2

## 🌍 Ethical Reflection
- Bias Risk: If dataset excludes rural smallholder farms, predictions may skew toward industrial farming.  

- Fairness: Ensure equal benefit across regions and crop types.  

- Sustainability: Better yield forecasting reduces waste, strengthens food systems, and supports SDG 2.  


## 📢 Citation
“AI can be the bridge between innovation and sustainability.” — UN Tech Envoy

---
