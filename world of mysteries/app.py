from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/characters")
def characters():
    return render_template("characters.html")


@app.route("/kingdoms")
def kingdoms():
    return render_template("kingdoms.html")


@app.route("/aura")
def aura():
    return render_template("aura.html")


@app.route("/sea-gates")
def sea_gates():
    return render_template("sea_gates.html")


@app.route("/chapters")
def chapters():
    return render_template("chapters.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)