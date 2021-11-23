from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'dgfjubdflgbdfsi'

@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def processing():
    session['name_input'] = request.form['name_input']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    name = session['name_input']
    location = session['location']
    language = session['language']
    comment = session['comment']
    return render_template('result.html', name=name, location=location, language=language, comment=comment)

if __name__ == "__main__":
    app.run(debug=True)
