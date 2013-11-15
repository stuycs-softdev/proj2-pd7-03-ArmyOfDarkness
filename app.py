from flask import Flask

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Temp home page for group 3</h1>"

if __name__ == "__main__":
    app.debug = True
    app.run(port=7003)
