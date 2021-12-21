from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import Users
from flask_app.models.recipe import Recipes

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
        'lname': request.form['lname']
    }
    user_id = Users.save(data)
    session['user_id'] = user_id
    return redirect(f'/profile/{user_id}')


@app.route('/login', methods=["POST"])
def user_login():
    if not Users.validate_login(request.form):
        return redirect('/')
    data = {'email': request.form['email']}
    user_with_email = Users.get_by_email(data)
    user_id = user_with_email.id
    if 'user_id' in session:
        return redirect(f'/profile/{user_id}')
    if user_with_email == False:
        flash("Invalid Email/Password.")
        return redirect('/')
    if not bcrypt.check_password_hash(user_with_email.password, request.form['password']):
        flash("Invalid Email/Password.")
        return redirect('/')
    session['user_id'] = user_id
    return redirect(f'/profile/{user_id}')

@app.route('/profile/<int:user_id>')
def user_profile(user_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id'],
        'user_id': user_id
    }
    one_user = Users.get_profile(data)
    one_recipe = Recipes.user_recipes()
    print(one_recipe)
    if one_user == False:
        return redirect(f'/profile/{user_id}')
    return render_template('profile.html', user_profile = one_user, one_recipe = one_recipe)

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')