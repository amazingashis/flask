from flask import Flask , render_template
from flask import request
from werkzeug.datastructures import RequestCacheControl
import model

app = Flask(__name__)



@app.route("/",methods = ['POST','GET'])
def marks():

    return render_template("index.html" )


@app.route('/sub', methods = ['POST'])
def submit():
    if request.method == "POST":
        size = request.form["size"]
        res = model.marks_prediction(size)
        siz = res
    return render_template("index.html", weight = siz )


if __name__ == "__main__":
    app.run()
  