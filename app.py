"""Flask app for adopt app."""

from flask import Flask, url_for, render_template, redirect, flash, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
# EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "abcdef"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
# db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.route("/")
def list_pets():
    """List all pets."""

    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route('/add', methods = ['GET', 'POST'])
def add_pet():
    """form  to add pet"""
    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect('/')
    else:
        return render_template('addPetForm.html', form = form)
    

@app.route('/<int:pet_id>')
def pet_profile(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet.html', pet = pet)


@app.route('/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)

    form = EditPetForm(obj=pet)  # Passing the pet object to the form

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.age = form.age.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect('/' + str(pet_id))

    return render_template('editPetForm.html', form=form, pet=pet)

@app.route('/<int:pet_id>/delete', methods=['POST'])
def delete_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)

    db.session.delete(pet)
    db.session.commit()
    print(f'pet id: {pet_id} has been deleted')

    return redirect('/')