from flask import Flask,render_template,json,request,jsonify
import os
import yaml
import pandas as pd
import numpy as np
import pickle
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer


app = Flask(__name__,template_folder="temp")



# model = pickle.load(open("/Users/bhikipallai/Desktop/Projects/Machine_Learning_Projects/saved_models/xgb_model.pkl","rb"))
# Update this line in your app.py
model = pickle.load(open("saved_models/xgb_model.pkl", "rb"))

# model = pickle.load(open("/app/saved_models/xgb_model.pkl","rb"))
scalar = pickle.load(open("saved_models/p1.pkl", "rb"))

@app.route("/",methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
    if request.method == "POST":
        pregnancies = float(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        blood_pressure = float(request.form['bloodPressure'])
        skin_thickness = float(request.form['skinThickness'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetes_pedigree_function = float(request.form['diabetesPedigreeFunction'])
        age = float(request.form['age'])

        data = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]],
                            columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

        data = scalar.transform(data)
        my_prediction = model.predict(data)

        if my_prediction == 1:
            my_prediction = "Sorry! you have Diabetic"
        else:
            my_prediction = "Congratulation! You are healthy"

        return render_template("result.html",prediction = my_prediction)





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)