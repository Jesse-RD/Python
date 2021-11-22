from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '123456789'

@app.route('/')
def page():
    session['count'] += 1
    return render_template('index.html')

@app.route('/count', methods=['POST'])
def counter():
    if request.form['addTwo']:
        session['count'] += 1
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def reset_counter():
    if request.form['reset']:
        session.clear()
        session['count'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)