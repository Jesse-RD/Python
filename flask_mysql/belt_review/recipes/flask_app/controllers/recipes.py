from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.recipe import Recipes
from flask_app.models.user import Users


@app.route('/new_recipe/<int:user_id>')
def create_recipe(user_id):
    user_id = session['user_id']
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id'],
        'user_id': user_id
    }
    one_user = Users.profile_recipes(data)
    print(one_user)
    return render_template('new_recipe.html', user_profile = one_user)

@app.route('/process_recipe', methods=['POST'])
def process_recipe():
    user_id = session['user_id']
    if not Recipes.validate_recipe(request.form):
        return redirect(f'/new_recipe/{user_id}')
    print(request.form)
    data = {
        'name': request.form['name'],
        'thirty': request.form['thirty'],
        'descr': request.form['descr'],
        'inst': request.form['inst'],
        'd_made': request.form['d_made'],
        'user_id': session['user_id']
    }
    Recipes.save_recipe(data)
    return redirect(f'/profile/{user_id}')

@app.route('/instructions/<int:user_id>/<int:recipe_id>')
def show_recipe(user_id, recipe_id):
    user_id = session['user_id']
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': recipe_id,
        'user_id': user_id
    }
    one_recipe = Recipes.get_recipe(data)
    if one_recipe == False:
        return redirect(f'/profile/{user_id}')
    return render_template('view_recipe.html', one_recipe = one_recipe, logged = user_id)

@app.route('/edit_recipe/<int:user_id>/<int:recipe_id>')
def edit_recipe(user_id, recipe_id):
    user_id = session['user_id']
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': recipe_id,
        session['user_id']: user_id
    }
    one_recipe = Recipes.get_recipe(data)
    logged_user = session['user_id']
    print(one_recipe)
    return render_template('edit_recipe.html', one_recipe = one_recipe, logged = logged_user)

@app.route('/update_recipe/<int:user_id>/<int:recipe_id>', methods=['POST'])
def update_recipe(user_id, recipe_id):
    user_id = session['user_id']
    if 'user_id' not in session:
        return redirect('/')
    if not Recipes.validate_recipe(request.form):
        return redirect(f'/edit_recipe/{user_id}')
    data = {
        'id': recipe_id,
        'name': request.form['name'],
        'thirty': request.form['thirty'],
        'descr': request.form['descr'],
        'inst': request.form['inst'],
        'd_made': request.form['d_made'],
        'user_id': session['user_id']
    }
    Recipes.update_recipe(data)
    return redirect(f'/profile/{user_id}')

@app.route('/delete_recipe/<int:user_id>/<int:recipe_id>', methods=['POST'])
def delete_recipe(user_id, recipe_id):
    user_id = session['user_id']
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': recipe_id
    }
    Recipes.delete_recipe(data)
    return redirect(f'/profile/{user_id}')
