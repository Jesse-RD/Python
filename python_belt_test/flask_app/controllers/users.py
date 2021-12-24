from flask_app import app
from flask import render_template, redirect, request, session
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models.sighting import Sighting
bcrypt = Bcrypt(app)

from flask_app.models.user import Users

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process_user', methods=['POST'])
def process_user():
    if not Users.validate_register(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        'email': request.form['email'],
        'password': pw_hash,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name']
    }
    user_id = Users.save(data)
    session['user_id'] = user_id
    return redirect(f'/dashboard/{user_id}')

@app.route('/login', methods=["POST"])
def user_login():
    if not Users.validate_login(request.form):
        return redirect('/')
    data = {'email': request.form['email']}
    user_with_email = Users.get_by_email(data)
    user_id = user_with_email.id
    if 'user_id' in session:
        return redirect(f'/dashboard/{user_id}')
    if user_with_email == False:
        flash("Invalid Email/Password.")
        return redirect('/')
    if not bcrypt.check_password_hash(user_with_email.password, request.form['password']):
        flash("Invalid Email/Password.")
        return redirect('/')
    session['user_id'] = user_id
    return redirect(f'/dashboard/{user_id}')

@app.route('/dashboard/<int:user_id>')
def user_profile(user_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    one_user = Users.get_profile(data)
    print("&&&&&&&&")
    print(one_user)
    one_sighting = Sighting.user_sighting(data)
    print(one_sighting)
    if one_user == False:
        return redirect(f'/dashboard/{user_id}')
    return render_template('dashboard.html', user_profile = one_user, one_sighting = one_sighting)

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')