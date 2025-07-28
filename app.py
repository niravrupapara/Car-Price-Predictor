
from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np


app = Flask(__name__)

model = pickle.load(open("linear_regression_model.pkl" ,'rb'))
df=pd.read_csv("clean_car_data.csv")



@app.route('/')

def home():

    companies = sorted(df['company'].unique())
    car_models = sorted(df['name'].unique())
    year = sorted(df['year'].unique() , reverse=True)
    fuel_type = df['fuel_type'].unique()
    companies.insert(0,"Select Company")

    return render_template('index.html' , companies = companies , car_models= car_models , years = year , fuel_types = fuel_type)

@app.route('/predict' , methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kilo_driven'))

    

    prediction = model.predict(pd.DataFrame([[car_model , company , year , kms_driven , fuel_type]] , columns=['name' , 'company' , 'year' , 'kms_driven' , 'fuel_type' ]))
    print(predict)
    price_in_lakh =  round(prediction[0]/100000 ,2)
    return f"₹ {price_in_lakh} Lakh"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
