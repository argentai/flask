from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_baby():
    return render_template('index.html')

@app.route("/1")
def hello_cute():
    return "<p>Hello Cute!  </p>"


if __name__=="__main__":
    app.run(debug=True)