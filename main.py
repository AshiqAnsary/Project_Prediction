
from distutils.debug import DEBUG
from urllib import request
from flask import Flask, render_template, request
import numpy as np
import sklearn
import pickle

app = Flask(__name__)

model=pickle.load(open("linear_model.pkl","rb"))


@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")


@app.route("/prediction",methods=["POST"])
def prediction():

    if request.method=="POST":
        age=request.form["age"]
        bmi=request.form["bmi"]
        children=request.form["children"]
        sex=request.form["sex"]
        smoker=request.form["smoker"]
        region=request.form["region"]

        predict=model.predict([[age,bmi,children,region,sex,smoker]])
        return render_template("index.html",predict="Your premium amount{}".format(predict))
    else:

            return render_template("index.html",predict="Not predictable")
        


if __name__ == "__main__":
    app.run(debug=True)
