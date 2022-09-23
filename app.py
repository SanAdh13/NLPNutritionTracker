from flask import Flask,render_template

#landing page
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/addFood")
def food():
    return hello world

@app.route("/track")
def track():
    return hello world


if __name__ = "__main__":
    