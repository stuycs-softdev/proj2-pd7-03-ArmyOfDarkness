from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def gmap(address):
    addr = address.replace(" ","+")
    return "http://maps.googleapis.com/maps/api/staticmap?center="+addr+"&zoom=4&size=600x600&maptype=roadmap&markers=color:blue%7Clabel:S%7C11211%7C11206%7C11222&sensor=false

if __name__ == "__main__":
    address = raw_input("Enter address: ")
    zip = raw_input("Enter zip code: ")
    location = googlemap(address,zip)
    print("maps.googleapis.com/maps/api/staticmap?center=" + address + " " + zip + "&markers=color:blue%7Clabel:S%7C11211%7C11206%7C11222" + address + " " + zip + "&zoom=14&size=600x600&sensor=false&key=AIzaSyC1KAwE3N0GcxPNGlWhjACaM7dFX_lFTB0")
