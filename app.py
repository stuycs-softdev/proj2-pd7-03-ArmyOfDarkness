#!/usr/bin/python

from flask import Flask, session, redirect, request, url_for, render_template
from education_backend import run, city_search, keytest
from myedu import uniSearch, imgSearch, depSearch, profSearch, courseSearch, getLink
import json 
import db
#import googlemap


app = Flask(__name__)
app.secret_key = "secretkey"

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html",loggedin='user' in session)
@app.route("/register", methods = ['GET', 'POST'])
def register():
    if 'user' in session:
        return redirect(url_for('home',loggedin=True))
    elif request.method == "GET":
        return render_template("register.html",message = "")
    else:
        button = request.form['button'].encode("utf8")
        if button == "Register":
            if db.register(request.form['user'], request.form['pass']):
                session['user'] = request.form['user']
                return redirect(url_for('home',loggedin=True))
            else:
                return render_template("register.html", message = "User already exists. Please login.")
                
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('home',loggedin=True))
    elif request.method == "GET":
        return render_template("login.html", message = "")
    else:
        user = request.form['user'].encode ('ascii',"ignore")
        pw = request.form['pass'].encode ('ascii',"ignore")
        if user == "" or pw == "":
            return render_template("login.html", message = "Please enter your username and password.")
        elif db.login(user, pw):
            session['user'] = user
            return redirect(url_for('home',loggedin=True))
        else:
            return render_template("login.html", message = "Invalid username and password combination. Usernames and passwords are case sensitive. Please try again.")

@app.route("/schoolsearch", methods = ['GET', 'POST'])
def search(): 
    if 'user' not in session:
        return redirect(url_for('login'))
    elif request.method == 'GET':
        return render_template("school_search.html",loggedin=True,message = "")
    else: 
        schoolid = request.form['schoolname']
        return redirect(url_for("schoolsearchresults",query=schoolid))

@app.route("/results/schoolsearch/?q=<query>")
@app.route("/results/schoolsearch/<name>")
@app.route("/results/schoolsearch/<name>/<dept>")
@app.route("/results/schoolsearch/<name>/<dept>/<prof>")
def schoolsearchresults(query=None,name=None,dept=None,prof=None):
    if query:
        d=uniSearch(query)
    else:
        link = getLink(name,dept,prof)
        if prof:
            d=courseSearch(link)
        elif dept:
            d=profSearch(link)
        elif name:
            d=depSearch(link)
    return render_template("schoolsearchresults.html",loggedin=True,query=query,name=name,dept=dept,prof=prof,d=d)

@app.route("/citysearch", methods = ['GET', 'POST'])
def citysearch():
    if 'user' not in session:
        return redirect(url_for('login'))
    elif request.method == 'GET':
        return render_template("city_search.html",loggedin=True)
    else: 
        city = request.form['city']
        zipcode = request.form['zipcode']
        state = request.form['state']
        key = "c7e0635761a449cde8a406b7b1eaaffb"
        print(key)

        if (' ' in city): 
            return render_template("cityError.html")
        elif (len(zipcode) != 0 and len(zipcode) != 5):
            return render_template("zipError.html")
        elif (len(state) != 0 and len(state) != 2): 
            return render_template("stateError.html")
        elif (keytest(city,state,zipcode,key) == False):
            return render_template("keyError.html")
        else: 
            d = city_search(city, state, zipcode,key)
            return render_template("results.html", d=json.dumps(d), message = "search complete",loggedin=True)

        
@app.route("/account", methods = ['GET', 'POST'])
def account():
    if 'user' in session:
        if request.method == 'GET': 
            return render_template("changepass.html",loggedin=True,message = "")
        else:
            user = session['user']
            old = request.form['old']
            new = request.form['new']
            if db.changePass(user, old, new):
                return render_template("changepass.html",loggedin=True, message = "Password changed successfully.")
            else:
                return render_template("changepass.html",loggedin=True,message = "Unsuccessful. You entered an incorrect password.")
    else: 
         return redirect(url_for('login'))
@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/mapsearch',methods=["POST","GET"])
def map():
    if 'user' not in session:
        return redirect(url_for('login'))
    elif request.method == 'GET':
        return render_template("map_search.html",loggedin=True)
    else:
        schoolname=request.form['schoolname']
        addr = schoolname.replace(" ","+")
        return render_template("map_search.html",addr = schoolname,loggedin=True)
        
if __name__ == "__main__":
    app.debug = True
    app.run(port=5005)
