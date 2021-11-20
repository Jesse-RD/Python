from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("index.html")

@app.route('/play/<int:num>')
def num_boxes(num):
    return render_template("indexTwo.html", num=num)

@app.route('/play/<int:num>/<color>')
def custom_boxes(num, color):
    return render_template("indexTwo.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)
