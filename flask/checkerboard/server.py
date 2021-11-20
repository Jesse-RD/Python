from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template("index_4x4.html")

@app.route('/<int:num>')
def checkersFour(num):
    return render_template("index_custom_rows.html", num=num)

@app.route('/<int:x>/<int:y>')
def checkerboard_custom(x, y):
    return render_template("index_custom_board.html", x=x, y=y)


if __name__=="__main__":
    app.run(debug=True)