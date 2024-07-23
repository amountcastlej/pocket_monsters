from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.pokemon import Pokemon 

@app.route('/')
def index():
    return render_template('index.html', pokemon = Pokemon.all_pokemon())

@app.route('/pokemon/new')
def pokemon_new():
    return render_template('new_pokemon.html')

@app.route('/pokemon/create', methods=['POST'])
def create_pokemon():
    Pokemon.create_pokemon(request.form)
    return redirect('/')

@app.route('/pokemon/edit/<int:pokemon_id>')
def edit_pokemon(pokemon_id):
    data={
        'id': pokemon_id
    }
    pokemon = Pokemon.one_pokemon(data)
    return render_template('edit_pokemon.html', pokemon = pokemon)

@app.route('/pokemon/<int:pokemon_id>')
def one_pokemon(pokemon_id):
    data={
        'id': pokemon_id
    }
    pokemon = Pokemon.one_pokemon(data)
    return render_template('one_pokemon.html', pokemon = pokemon)

@app.route('/pokemon/update/<int:pokemon_id>', methods=['POST'])
def update_pokemon(pokemon_id):
    Pokemon.update(request.form, id)
    return redirect('/')

@app.route('/pokemon/<int:pokemon_id>/delete')
def destroy_pokemon(pokemon_id):
    data={
        'id': pokemon_id
    }
    Pokemon.destroy_pokemon(data)
    return redirect('/')