from flask import Flask, render_template, jsonify, request,redirect
from utils import MedicalInsurance
import numpy as np
import config


app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to Medicle Insurance Charges Prediction")
    return render_template("home.html")

@app.route('/prediction',methods = ['GET','POST'])
def prediction():
    if request.method == 'POST':
        data = request.form

        print('data:',data)

        med_ins = MedicalInsurance(data)

        price = med_ins.get_predicted_price()
        print(price)
        #return jsonify({"Price:":price})
        return render_template("home.html", prediction = price)
        
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5004,debug = True)    
        