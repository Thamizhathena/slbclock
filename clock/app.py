"""
code for calculate angle
"""
from flask import Flask, render_template, request
from clock import Clock_Angle
app = Flask(__name__)

@app.after_request
def add_header(newr):
    """
    to add header
    """
    newr.headers["Pragma"] = "no=cache"
    newr.headers["Expires"] = "0"
    newr.headers["Cache-Control"] = "public, max-age=0"
    return newr

@app.route("/home", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])

def home():
    """
    home to calculate angle
    """
    answer = ""
    if "fHour" in request.form and "fMins" in request.form:
        hour = float(request.form["fHour"])
        minutes = float(request.form["fMins"])
        answer = Clock_Angle(hour, minutes).calAngle()
    return render_template("Home.html", pageData=str(answer))

if __name__ == '__main__':
     APP.run(host='0.0.0.0', debug=True)
