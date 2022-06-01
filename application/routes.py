from flask import render_template

from application import app
#home get route
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')
# routes.py - called by the user in browser via url which renders the template

@app.route('/favourites')
def favourites():
    return render_template('favourites.html', title='favourites', favourites = ['shopping','Doing nails','watching Netflix','sleeping'])