#import library mandatory
from flask import Flask, render_template

app = Flask("my_first_app")

#creates an index
@app.route("/")
def say_hello():
  return render_template("index.html")

#so that the app actually runs
app.run(debug=True)