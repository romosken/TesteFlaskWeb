from flask import Flask, app, render_template

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def hello():
    return render_template('hello.html')
