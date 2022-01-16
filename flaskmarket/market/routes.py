from market import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from market.models import Items, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')


@app.route("/market")
# Below decorator ensure that user is logged in before accessing market page...We can force unauthorized user to
# to land on login page by making change in __init__ file in login manager
@login_required
def market_page():
    items = Items.query.all()
    return render_template('market.html', items=items)


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_add=form.email_address.data,
                              password=form.password1.data)
        # print(f'Just printing plain text user provided password from form before hashing> {form.password1.data}')
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfully. You are now logged in as: {user_to_create.username}', category="success")
        return redirect(url_for('market_page'))
    if form.errors != {}:  # If error received from form validator class
        for err_msg in form.errors.values():
            flash(err_msg, category='danger')

    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):

            login_user(attempted_user)
            flash(f'Welcome! You are now logged in as: {attempted_user.username}', category='success')

            return redirect(url_for('market_page'))

        else:
            flash(f'Username or password is incorrect. Please try again', category='danger')

    return render_template('login.html', form=form)


@app.route("/logout")
def logout_page():
    logout_user()
    flash(f'You have been logged out', category='info')
    return redirect(url_for('home_page'))


# dynamic routing example....here we can pass any dynamic value as string like below...that's what facebook does
@app.route("/about/<username>")
def about(username):
    return f'Hello {username} you are visiting about page'
