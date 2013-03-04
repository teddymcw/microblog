from flask import render_template, flash, redirect
from app1 import app1
from forms import LoginForm


@app1.route('/')
@app1.route('/index')
def index():
	user = { 'nickname': 'Dike' } # fake user
	posts = [ # fake array of posts
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengerrrs movie was so cool!' 
        }
    ]
	return render_template("index.html",
		title = 'Home', 
		user = user,
		posts = posts)

@app1.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="' + form.openid.data +
		'", remember_me=' + str(form.remember_me.data))
		return redirect('/index')
	return render_template('login.html', 
		title = 'Sign In', 
		form = form
		providers = app.config['OPENID_PROVIDERS'])







