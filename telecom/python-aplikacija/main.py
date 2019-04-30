from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

    varijabla1 = "Učimo Python!"

    proizvodi = ["Monitor", "Tipkovnica", "Miš"]

    return render_template("index.html", varijabla1=varijabla1, proizvodi=proizvodi)

@app.route("/o-nama")
def onama():
    return render_template("o-nama.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")


if __name__ == '__main__':
    app.run()