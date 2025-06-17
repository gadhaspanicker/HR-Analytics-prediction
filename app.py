from flask import Flask, render_template, request
import joblib
import numpy as np

# Create a Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('hranalyticsmodel.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        gender = int(request.form['gender'])
        city = int(request.form['city'])
        jobtitle = int(request.form['jobtitle'])
        departmentname = int(request.form['departmentname'])
        storelocation = int(request.form['storelocation'])
        division = int(request.form['division'])
        age = float(request.form['age'])
        lengthservice = float(request.form['lengthservice'])
        businessunit = int(request.form['businessunit'])
        
        # Correct feature order
        features = np.array([[gender, city, jobtitle, departmentname, storelocation, division, age, lengthservice, businessunit]])
        
        prediction = model.predict(features)
        
        return render_template('index.html', prediction_text=f'Predicted Absent Hours: {prediction[0]:.2f}')

if __name__ == "__main__":
    app.run(debug=True)