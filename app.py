from flask import Flask, session, redirect, request, url_for, render_template
import db
app = Flask(__name__)
app.secret_key = "secretkey"

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")
    
@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.debug = True
    app.run(port=7003)
