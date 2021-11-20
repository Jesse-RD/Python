from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def name(name):
    return f"Hi {name}"

@app.route('/repeat/<num>/<element>')
def repeat(num, element):
    return element * int(num)

@app.route('/<error>')
def error(error):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)