from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import Users
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def create_user():
    return render_template("register.html")

@app.route('/process_user', methods=['POST'])
def process_user():
    if not Users.validate_register(request.form):
        return redirect('/register')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        'email': request.form['email'],
        'password': pw_hash,
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'dob': request.form['dob'],
        'fav_language': request.form['fav_language']
    }
    user_id = Users.save(data)
    Users.save(request.form)
    return redirect('/')


@app.route('/login', methods=["POST"])
def user_login():
    data = {'email': request.form['email']}
    user_with_email = Users.get_by_email(data)
    if user_with_email == False:
        flash("Invalid Email/Password.")
        return redirect('/')
    if not bcrypt.check_password_hash(user_with_email.password, request.form['password']):
        flash("Invalid Email/Password.")
        return redirect('/')
    session['user_id'] = user_with_email.id
    user_id = user_with_email.id
    return redirect('/profile')

@app.route('/profile')
def user_profile():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    one_user = Users.get_profile(data)
    print(one_user)
    return render_template('profile.html', user_profile = one_user)

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')