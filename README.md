fish-kill-prediction
│
├── data
│   ├── raw
│   └── processed
│
├── notebooks
│
├── src
│
├── models
│
├── results
│
├── README.md
└── requirements.txt


VSCODE  extensions:
Python
Jupyter
Pylance

SetUp Python Environment:
python -m venv venv
venv\Scripts\activate
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
pip install xgboost tensorflow
pip freeze > requirements.txt