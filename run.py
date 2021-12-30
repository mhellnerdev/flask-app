from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return '<h1>Interior Crocodile Alligator</h1>'


@app.route('/information')
def info():
    return "<h1>I Drive a Chevy Movie Theater</h1>"


if __name__ == '__main__':
    app.run(debug=True)
else:
    print('fail')
