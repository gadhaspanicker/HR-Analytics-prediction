
# 🧠 HR Analytics Prediction App

A simple Flask web application that predicts employee absent hours based on input features using a pre-trained machine learning model.

## 🚀 Features
- Web form for input
- Predicts absent hours using `hranalyticsmodel.pkl`
- Built with Flask, NumPy, and Joblib

## 📦 Requirements
- Python 3
- Flask
- NumPy
- Joblib

## 🔧 How to Run

```bash
pip install flask numpy joblib
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📁 Files
- `app.py` – Flask app
- `hranalyticsmodel.pkl` – Trained ML model
- `templates/index.html` – HTML form

## 🛠 Tip
Use `__name__` (double underscores) instead of `_name_` in Flask setup:
```python
app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)
```
