# 🌾 AI for Zero Hunger: Crop Yield Prediction (SDG 2)

This project applies **Machine Learning** to support **UN SDG 2 (Zero Hunger)** by predicting crop yields from weather, soil, and fertilizer data.

---

## 🚀 Overview
- **Problem:** Farmers face unpredictable harvests due to climate change and poor resource planning.  
- **Solution:** An ML model to predict yields → reduces waste, improves food security.  
- **Approach:** Supervised Learning (Regression).  
- **Algorithms:** Linear Regression, Random Forest.  
- **Dataset:** Open agriculture datasets (sample CSV included).  

---

## 📂 Repo Structure
ai-sdg2-crop-yield/
├── data/ # Dataset
├── notebooks/ # Jupyter Notebook
├── scripts/ # Python script
├── results/ # Graphs + metrics
├── README.md # Project intro
├── REPORT.md # 1-page summary
└── PITCH_DECK.pdf # Pitch slides

---

## ⚙️ How to Run
```bash
git clone https://github.com/yourusername/ai-sdg2-crop-yield.git
cd ai-sdg2-crop-yield
pip install -r requirements.txt
python scripts/crop_yield_predictor.py
```
Or open the notebook in Google Colab/Jupyter.

## 📊 Example Results
Random Forest outperformed Linear Regression.

Metrics (sample):

MAE: 0.08

RMSE: 0.12

R²: 0.96

Visualization (Predicted vs Actual):

## 🌍 Ethical Reflection
Bias risk: If dataset excludes rural smallholder farms.

Fairness: Ensure equal benefit across regions.

Sustainability: Better planning → less waste, stronger food systems.

## 📢 Citation
“AI can be the bridge between innovation and sustainability.” — UN Tech Envoy

