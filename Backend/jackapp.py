#!/usr/bin/python

from flask import Flask, session, redirect, request, url_for, render_template
from education_backend import run, citysearch
import json 

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route("/")
@app.route("/home")
def home(): 
    return "<h1>Home</h1>"

@app.route("/search", methods = ['GET', 'POST'])
def city_search():
    if request.method == 'GET':
        return render_template("city_search.html", message = "")
    else: 
        city = request.form['city']
        zipcode = request.form['zipcode']
        state = request.form['state']
        #return "<h1>Home</h1>"
        d = citysearch(city, state, zipcode)
        #return redirect(url_for('results'), d=d)
        return render_template("results.html", d=json.dumps(d), message = "search complete")
        print("begin")
       # print(str(d))

@app.route("/results", methods = ['GET', 'POST'])
def results(): 
    if request.method == 'GET': 
        return render_template("results.html", d=JSON.dumps(d), message = "search complete")


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=5005)
