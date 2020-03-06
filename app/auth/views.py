from flask import render_template, url_for, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user
from . import auth
from .forms import LoginForm, RegistrationForm
from ..email import send_email
from ..models import Fan
from .. import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Fan.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.home')
            return redirect(next)
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash("You've been logged out.")
    return redirect(url_for('main.home'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Fan(email=form.email.data,
                   username=form.username.data,
                   password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Coolio. Now you can login.")
        # since form input is valid (not an existing user, etc),
        # we can send them a welcome email
        if current_app.config['RAGTIME_ADMIN']:
            send_email(current_app.config['RAGTIME_ADMIN'],
                        'New User',
                        'mail/new_user',
                        user=user)
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)