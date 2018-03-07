from flask import Flask, render_template
import models
import stores
from dummy_data import post_store

app = Flask(__name__)

@app.route("/")
@app.route("/index")

def home():
    return render_template("index.html", posts = post_store.get_all())

if __name__ == '__main__':
   app.run(debug = True)
