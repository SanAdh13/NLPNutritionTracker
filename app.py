from flask import Flask,render_template
app = Flask(__name__)

#landing page
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/addFood")
def food():
    return 0

@app.route("/track")
def track():
    return 0


if __name__ == "__main__":
    app.run(debug=True)