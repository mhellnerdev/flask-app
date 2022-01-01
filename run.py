from flask import Flask

app = Flask(__name__)


# the string operator that is passed into the function decorator here will create a route to the flask "view"
@app.route("/")
def index():
    return '<h1>Interior Crocodile Alligator</h1>'


# the string operator that is passed into the function decorator here will create a route to the flask "view"
@app.route('/information')
def info():
    return "<h1>I Drive a Chevy Movie Theater</h1>"


if __name__ == '__main__':
    app.run(debug=True)
else:
    print('There was an error launching run.py')
