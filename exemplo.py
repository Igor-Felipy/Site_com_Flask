from flask import Flask, render_template

app = Flask(__name__)

postagens = [{"titulo":"Criar site","autor":"Igor"},{"titulo":"testando site","autor":"Felipy"}]


@app.route("/")
def index():
    var = '<h1>sou uma informação</h1>'
    return render_template("index.htm", var=var, postagens=postagens)

@app.route("/about")
def about():
    return render_template("about.htm")


if __name__ == "__main__":
    app.run(debug=True)