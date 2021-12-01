from flask import Flask, render_template, redirect, request, session

from create_users import Users
app = Flask(__name__)

@app.route('/')
def user_list():
    users = Users.get_all()
    return render_template('Read (All).html', users=users)

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


if __name__ == '__main__':
    app.run(debug=True)