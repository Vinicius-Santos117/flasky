from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Bem-vindo à minha aplicação Flask no PythonAnywhere!</h1>"

@app.route("/sobre")
def sobre():
    return "<p>Essa é a página Sobre.</p>"

if __name__ == "__main__":
    app.run()
