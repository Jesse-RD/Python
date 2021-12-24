from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.sighting import Sighting
from flask_app.models.user import Users

@app.route('/new_sighting/<int:user_id>')
def create_sighting(user_id):
    user_id = session['user_id']
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id'],
        'user_id': user_id
    }
    one_user = Users.user_for_sighting(data)
    print(one_user)
    return render_template('new_sighting.html', user_profile = one_user)

@app.route('/process_sighting', methods=['POST'])
def process_sighting():
    user_id = session['user_id']
    if not Sighting.validate_sighting(request.form):
        return redirect(f'/new_sighting/{user_id}')
    print(request.form)
    data = {
        'location': request.form['location'],
        'description': request.form['description'],
        'date': request.form['date'],
        'num_sightings': request.form['num_sightings'],
        'user_id': session['user_id']
    }
    print(data)
    Sighting.save_sighting(data)
    return redirect(f'/dashboard/{user_id}')

@app.route('/show_sighting/<int:user_id>/<int:sighting_id>')
def show_sighting(user_id, sighting_id):
    user_id = session['user_id']
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': sighting_id,
        'user_id': user_id,
        'id_num': sighting_id
    }
    one_sighting = Sighting.get_sighting(data)
    sighting_user = Sighting.get_user_for_sighting(data)
    reporter = Sighting.reporter(data)
    print("*************************")
    print(sighting_user[0])
    if one_sighting == False:
        return redirect(f'/dashboard/{user_id}')
    return render_template('show_sighting.html', one_sighting = one_sighting, user = sighting_user, logged = user_id, reporter = reporter)

@app.route('/edit_sighting/<int:user_id>/<int:sighting_id>')
def edit_sighting(user_id, sighting_id):
    user_id = session['user_id']
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': sighting_id,
        'user_id': user_id,
        'id_num': sighting_id
    }
    one_sighting = Sighting.get_sighting(data)
    sighting_user = Sighting.get_user_for_sighting(data)
    return render_template('edit_sighting.html', one_sighting = one_sighting, logged = user_id, user = sighting_user)

@app.route('/update_sighting/<int:user_id>/<int:sighting_id>', methods=['POST'])
def update_recipe(user_id, sighting_id):
    user_id = session['user_id']
    if 'user_id' not in session:
        return redirect('/')
    if not Sighting.validate_sighting(request.form):
        return redirect(f'/edit_sighting/{user_id}/{sighting_id}')
    data = {
        'id': sighting_id,
        'location': request.form['location'],
        'description': request.form['description'],
        'date': request.form['date'],
        'num_sightings': request.form['num_sightings'],
        'user_id': session['user_id']
    }
    Sighting.update_sighting(data)
    return redirect(f'/dashboard/{user_id}')

@app.route('/delete_sighting/<int:user_id>/<int:sighting_id>', methods=['POST'])
def delete_sighting(user_id, sighting_id):
    user_id = session['user_id']
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': sighting_id
    }
    Sighting.delete_sighting(data)
    return redirect(f'/dashboard/{user_id}')
