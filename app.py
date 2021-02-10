import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import model

app= Flask(__name__, static_url_path='/static')
my_model=pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def predictionpage():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    input_values = [float(i) for i in request.form.values()]  #fetching the input values
    df_row=[[i] for i in input_values]                        #This will form the input row
    df_keys = [i for i in request.form.keys()]    #fetching the input keys
    rescaling_cols=['temp', 'hum', 'windspeed']          #declaring list of keys which has to be rescaled

    #Declaring dictionary to convert into dataframe in the next step.
    df_dict = {df_keys[i]: df_row[i] for i in range(len(df_keys))}

    df=pd.DataFrame(df_dict)
    df[df.columns[df.columns.isin(rescaling_cols)]] = model.scaler.transform(df[df.columns[df.columns.isin(rescaling_cols)]])

    #Prediction of the trained model
    prediction= my_model.predict(df)
    #Output derived from the ML model
    output= round(prediction[0], 2)

    #Output sent to the html page
    return render_template('index.html', prediction_text='Prediction: {} cycle rents.'.format(output))

if __name__=="__main__":
    app.run(debug=True)