from flask import Flask, session, redirect, request, url_for, render_template
import db
import googlemap
app = Flask(__name__)
app.secret_key = "secretkey"

@app.route("/")
@app.route("/home")
def home():
    if 'user' in session:
        return render_template("index.html", user = session['user'])
    else:
        return redirect(url_for('login'))
        
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

@app.route("/account", methods = ['GET', 'POST'])
def account():
    if 'user' not in session:
        return redirect(url_for('login'))
    elif request.method == "GET":
        return render_template("account.html", message = "")
    else:
        user = session['user']
        old = request.form['old']
        new = request.form['new']
        if db.changePass(user, old, new):
            return render_template("account.html", message = "Password changed successfully.")
        else:
            return render_template("account.html", message = "Unsuccessful. You entered an incorrect password.")

@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/maps',methods=["POST","GET"])
def map():
    if request.method == 'GET':
            return render_template("map.html")
        
if __name__ == "__main__":
    app.debug = True
    app.run(port=7003)
