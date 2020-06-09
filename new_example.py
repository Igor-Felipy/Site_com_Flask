from flask import Flask, render_template

app = Flask(__name__)


@app.route("/teste")
def index():
    return render_template("new_site.html")


if __name__ == "__main__":
    app.run(debug=True)