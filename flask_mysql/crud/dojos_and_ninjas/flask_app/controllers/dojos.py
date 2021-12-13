from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojos

@app.route('/')
def all_dojos():
    dojos = Dojos.all_dojos()
    return render_template('dojos.html', dojos = dojos)

@app.route('/process_dojo', methods=['POST'])
def process_user():
    data = {
        'dname': request.form['dname'],
    }
    Dojos.save_dojo(data)
    return redirect('/')

@app.route('/dojo/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {
        'id': dojo_id
    }
    dojo = Dojos.dojo_with_ninjas(data)
    print("I have received from my class...")
    print(dojo)
    return render_template('dojo.html', dojo = dojo)