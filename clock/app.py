"""
high level support for doing this and that.
"""
from flask import Flask, render_template, request
from clock import Clock_Angle
app = Flask(__name__)

@app.after_request
def add_header(newr):
    """
    high level support for doing this and that.
    """
    newr.headers["Pragma"] = "no=cache"
    newr.headers["Expires"] = "0"
    newr.headers["Cache-Control"] = "public, max-age=0"
    return newr

@app.route("/home", methods=["GET","POST"])
@app.route("/", methods=["GET","POST"])

def home():
    """
    high level support for doing this and that.
    """
    answer = ""
    if "fHour" in request.form and "fMins" in request.form:
        hour = float(request.form["fHour"])
        minutes = float(request.form["fMins"])                 
        answer = Clock_Angle(hour,minutes).calAngle()
    return render_template("Home.html", pageData=str(answer))

if __name__ == "__main__":
    app.run(port=80)
