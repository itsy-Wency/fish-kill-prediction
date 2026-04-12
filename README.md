# Fish Kill Prediction

A complete project for predicting fish kill events in aquaponics systems using water-quality data, machine learning, and time-series forecasting.

---

## 🚀 Project Summary

This repository combines data engineering, model training, and forecasting to provide both:

- **Real-time fish kill risk detection** using classification models
- **Short-term dissolved oxygen forecasting** using ARIMA

The result is a practical workflow for early warning and pond management.

---

##  Repository Structure

- `data/raw` — original raw datasets
- `data/processed` — cleaned and merged data ready for analysis
- `notebooks` — Jupyter notebooks for data merging, cleaning, modeling, and evaluation
- `models` — exported model artifacts (`.pkl` files)
- `results` — charts, evaluation tables, and output summaries
- `src` — supporting project code
- `save_models.py` — script for training and saving model files

---

## 🔧 What’s Included

### Data
- Raw pond sensor and water-quality measurements
- Processed datasets with engineered features

### Notebooks
- `01_data_merge.ipynb` — merge and align datasets
- `02_data_cleaning.ipynb` — clean and prepare data
- `03_exploratory_analysis.ipynb` — explore patterns and distributions
- `04_model_fish_kill_prediction.ipynb` — train classification models
- `05_evaluation_and_results.ipynb` — evaluate model performance and forecast DO

### Models
- `models/random_forest.pkl`
- `models/xgboost.pkl`
- `models/arima_model.pkl`

### Scripts
- `save_models.py` — train and export models to the `models/` folder

---

## 📊 Model Performance

| Model         | Accuracy | Precision (Fish Kill) | Recall (Fish Kill) | F1-score |
|--------------|---------:|----------------------:|-------------------:|---------:|
| Random Forest | 0.89     | 1.00                  | 0.73               | 0.84     |
| XGBoost       | 0.89     | 1.00                  | 0.73               | 0.84     |

### Key insights
- The models are very precise at predicting fish kill events.
- Recall is moderate, indicating some risk events are not detected.
- `dissolved_oxygen` and `ammonia` are the strongest predictors.

---

## 🧪 Sample Output

```text
Model            Accuracy  Precision  Recall  F1-score
---------------------------------------------------
Random Forest    0.89      1.00       0.73    0.84
XGBoost          0.89      1.00       0.73    0.84
```

```text
Forecasted DO over next 24 hours:
2026-04-12 13:00:00    3.12
2026-04-12 14:00:00    2.98
2026-04-12 15:00:00    2.82
...
Forecasted fish_kill_risk:
2026-04-12 13:00:00    0
2026-04-12 14:00:00    1
2026-04-12 15:00:00    1
```

---

## 📈 Visualization

The notebooks include the following charts:

- Feature importance for classifier models
- Dissolved oxygen forecast over time

### Example visuals

Actual sample charts are available in the `images/` folder.

![Feature Importance](images/Feature%20Importance.png)

![Dissolved Oxygen Forecast ARIMA](images/Dissolved%20Oxygen%20Forecast%20ARIMA.png)

> These images are stored in the repository and render directly in GitHub.

---

## ⚙️ Setup Instructions

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## ▶️ How to Use

1. Run notebooks in order from `01_data_merge.ipynb` to `05_evaluation_and_results.ipynb`.
2. Execute:

```bash
python save_models.py
```

3. Review `models/` for exported `.pkl` files and `notebooks/05_evaluation_and_results.ipynb` for metrics and charts.

---

## 📌 Notes

This project is designed for aquaponics monitoring and fish kill risk management. It supports both current condition detection and short-term oxygen forecasting for proactive action.

