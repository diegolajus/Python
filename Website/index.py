from flask import Flask

app = Flask(__name__)

#crear rutas (decorador)
@app.route("/")
def home():
    return

# https://www.youtube.com/watch?v=fxavwHPJ36o