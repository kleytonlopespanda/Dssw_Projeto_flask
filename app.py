from flask import Flask
app = Flask(__name__)
@app.route('/')
def ola():
    return'<h1>olá, mundo!</h1>'
app.run()
