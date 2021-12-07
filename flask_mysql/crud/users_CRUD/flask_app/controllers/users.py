from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import Users

@app.route('/')
def user_list():
    users = Users.get_all()
    return render_template('Read (All).html', users = users)

@app.route('/create_user')
def create_user():
    return render_template("create_user.html")

@app.route('/process_user', methods=['POST'])
def process_user():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    Users.save(data)
    return redirect('/')

@app.route('/show_user/<int:user_id>')
def show_user(user_id):
    data = {
        'id': user_id
    }
    one_user = Users.get_one(data)
    print(one_user)
    return render_template('show_user.html', one_user = one_user)

@app.route('/edit_user/<int:user_id>')
def edit_user(user_id):
    data = {
        'id': user_id
    }
    one_user = Users.get_one(data)
    print(one_user)
    return render_template('edit_user.html', one_user = one_user)

@app.route('/delete_user/<int:user_id>', methods=['POST', 'GET'])
def del_user(user_id):
    data = {
        'id': user_id
    }
    one_user = Users.del_one(data)
    print(one_user)
    return redirect('/')

@app.route('/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    data = {
        'id': user_id,
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    one_user = Users.edit(data)
    print(one_user)
    return redirect(f'/show_user/{user_id}')