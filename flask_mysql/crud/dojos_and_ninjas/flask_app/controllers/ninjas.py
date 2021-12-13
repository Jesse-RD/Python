from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojos


@app.route('/new_ninja')
def new_ninja():
    dojos = Dojos.all_dojos()
    return render_template('new_ninja.html', all_dojos = dojos)

@app.route('/create/new_ninja', methods=['POST'])
def createNinja():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'age': request.form['age'],
        'dojos_id': request.form['dojos_id']
    }
    Ninja.save_ninja(data)
    dojos_id = request.form['dojos_id']
    return redirect(f'/dojo/{dojos_id}')