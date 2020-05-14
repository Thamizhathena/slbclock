from flask import Flask,render_template,json,request
from clock import Clock_Angle
app = Flask(__name__)

@app.after_request
def add_header(r):
    r.headers["Pragma"] = "no=cache"
    r.headers["Expires"]="0"
    r.headers["Cache-Control"] = "public, max-age=0"
    return r



@app.route("/home",methods=["GET","POST"])
@app.route("/",methods=["GET","POST"])
def home():
    answer = ""
    if "fHour" in request.form and "fMins" in request.form:        
        answer = str(Clock_Angle(float(request.form["fHour"]),float(request.form["fMins"])).calAngle())
        print(answer)
    return render_template("Home.html",pageData=str(answer))

if __name__=="__main__":
    app.run(port=80)