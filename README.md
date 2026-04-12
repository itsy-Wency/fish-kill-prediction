<style>
  .hero {background:#0b1f3f;color:#f8fbff;padding:24px;border-radius:16px;margin-bottom:24px;}
  .hero h1 {margin:0;font-size:2.4rem;}
  .hero p {margin:12px 0 0;max-width:760px;line-height:1.7;}
  .grid {display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px;margin:24px 0;}
  .card {background:#13294e;color:#eef3fd;padding:18px;border-radius:14px;box-shadow:0 16px 40px rgba(7,18,38,.18);}
  .card h3 {margin-top:0;font-size:1.2rem;}
  .badge {display:inline-block;background:#18a0fb;color:#fff;padding:6px 12px;border-radius:999px;font-size:.8rem;margin:3px 4px 3px 0;}
  .output {background:#071828;color:#d8e8ff;padding:18px;border-radius:14px;border:1px solid rgba(255,255,255,.08);}
  .tech-list {list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:8px;}
</style>

<div class="hero">
  <h1>Fish Kill Prediction</h1>
  <p>A comprehensive aquaponics monitoring project that combines data engineering, machine learning, and time-series forecasting to predict fish kill risk in pond systems.</p>
</div>

## Project Overview

This repository contains a complete end-to-end solution for predicting fish kill events using sensor and water quality data. The workflow includes:

- ingesting and cleaning raw pond datasets
- feature engineering for temporal and environmental signals
- training classification models for risk detection
- forecasting dissolved oxygen with ARIMA for early warning
- exporting model artifacts for deployment

## Key Components

<div class="grid">
  <div class="card">
    <h3>Data</h3>
    <p>Contains raw and processed datasets used for training and evaluation.</p>
    <span class="badge">data/raw</span>
    <span class="badge">data/processed</span>
  </div>
  <div class="card">
    <h3>Notebooks</h3>
    <p>Jupyter notebooks document the full analysis pipeline from merging data to model evaluation.</p>
    <span class="badge">01_data_merge.ipynb</span>
    <span class="badge">05_evaluation_and_results.ipynb</span>
  </div>
  <div class="card">
    <h3>Models</h3>
    <p>Serialized model files saved to the `models/` folder for easy reuse.</p>
    <span class="badge">random_forest.pkl</span>
    <span class="badge">xgboost.pkl</span>
    <span class="badge">arima_model.pkl</span>
  </div>
  <div class="card">
    <h3>Scripts</h3>
    <p>Utility scripts for exporting model artifacts and preparing the workspace.</p>
    <span class="badge">save_models.py</span>
  </div>
</div>

## Folder Structure

- `data/raw` — raw data files from the original collection
- `data/processed` — cleaned and merged datasets ready for modeling
- `notebooks` — analysis and modeling notebooks
- `models` — serialized model files saved as `.pkl`
- `results` — charts, tables, and evaluation outputs
- `src` — supporting source code for the project
- `save_models.py` — script to train and export models

## Model Performance Summary

<div class="output">
<strong>Random Forest</strong><br>
Accuracy: <strong>0.89</strong><br>
Precision (Fish Kill): <strong>1.00</strong><br>
Recall (Fish Kill): <strong>0.73</strong><br>
F1-score: <strong>0.84</strong>
</div>

<div class="output" style="margin-top:16px;">
<strong>XGBoost</strong><br>
Accuracy: <strong>0.89</strong><br>
Precision (Fish Kill): <strong>1.00</strong><br>
Recall (Fish Kill): <strong>0.73</strong><br>
F1-score: <strong>0.84</strong>
</div>

### Insights

- The models are highly precise at identifying fish kill events.
- Some risk cases remain undetected, which is reflected by the recall of `0.73`.
- `dissolved_oxygen` and `ammonia` are the most important predictors.

## Sample Output

<div class="output">
<pre>
Model            Accuracy  Precision  Recall  F1-score
---------------------------------------------------
Random Forest    0.89      1.00       0.73    0.84
XGBoost          0.89      1.00       0.73    0.84
</pre>
</div>

<div class="output" style="margin-top:16px;">
<pre>
Forecasted DO over next 24 hours:
2026-04-12 13:00:00    3.12
2026-04-12 14:00:00    2.98
2026-04-12 15:00:00    2.82
... 
Forecasted fish_kill_risk:
2026-04-12 13:00:00    0
2026-04-12 14:00:00    1
2026-04-12 15:00:00    1
</pre>
</div>

## Setup Instructions

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## How to Use

1. Run the notebooks in order from `01_data_merge.ipynb` through `05_evaluation_and_results.ipynb`.
2. Execute `python save_models.py` to train and export models into the `models/` folder.
3. Review the evaluation notebook for performance metrics and charts.

## Visualization

The notebooks include plots for:

- feature importance
- classification performance
- dissolved oxygen forecasting
- actual vs forecasted DO timelines

## Visualization Examples

<div class="grid">
  <div class="card">
    <h3>Feature Importance</h3>
    <p>A bar chart showing the most important predictors for fish kill events, such as dissolved oxygen and ammonia.</p>
    <img src="https://via.placeholder.com/600x320?text=Feature+Importance+Chart" alt="Feature importance chart" style="width:100%;border-radius:12px;margin-top:12px;">
  </div>
  <div class="card">
    <h3>DO Forecast</h3>
    <p>An example time-series chart forecasting dissolved oxygen levels and risk thresholds over the next 24 hours.</p>
    <img src="https://via.placeholder.com/600x320?text=Dissolved+Oxygen+Forecast" alt="Dissolved oxygen forecast chart" style="width:100%;border-radius:12px;margin-top:12px;">
  </div>
</div>

> Replace placeholder images with actual notebook chart exports once available.

## Notes

This project is designed for aquaponics and pond monitoring applications. It supports both immediate fish kill detection and short-term dissolved oxygen forecasting for early warning.
