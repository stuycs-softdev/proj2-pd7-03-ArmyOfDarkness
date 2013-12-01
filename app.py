#!/usr/bin/python

from flask import Flask, session, redirect, request, url_for, render_template
from education_backend import run, citysearch
import json 
import db

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")    
@app.route("/register", methods = ['GET', 'POST'])
def register():
    if 'user' in session:
        return redirect(url_for('home'))
    elif request.method == "GET":
        return render_template("register.html", message = "")
    else:
        button = request.form['button'].encode("utf8")
        if button == "Register":
            if db.register(request.form['user'], request.form['pass']):
                session['user'] = request.form['user']
                return redirect(url_for('home'))
            else:
                return render_template("register.html", message = "User already exists. Please login.")
        else:
            return render_template("register.html", message = "")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('home'))
    elif request.method == "GET":
        return render_template("login.html", message = "")
    else:
        user = request.form['user']
        pw = request.form['pass']
        if user == "" or pw == "":
            return render_template("login.html", message = "Please enter your username and password.")
        elif db.login(user, pw):
            session['user'] = user
            return redirect(url_for('home'))
        else:
            return render_template("login.html", message = "Invalid username and password combination. Usernames and passwords are case sensitive. Please try again.")

@app.route("/search", methods = ['GET', 'POST'])
def search(): 
    return render_template("index.html")

@app.route("/citysearch", methods = ['GET', 'POST'])
def citysearch():
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

@app.route("/account", methods = ['GET', 'POST'])
def account():
    if 'user' not in session:
        return redirect(url_for('login'))
    elif request.method == "GET":
        return render_template("changepass.html", message = "")
    else:
        user = session['user']
        old = request.form['old']
        new = request.form['new']
        if db.changePass(user, old, new):
            return render_template("changepass.html", message = "Password changed successfully.")
        else:
            return render_template("changepass.html", message = "Unsuccessful. You entered an incorrect password.")

@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
        
if __name__ == "__main__":
    app.debug = True
    app.run(port=7009)
