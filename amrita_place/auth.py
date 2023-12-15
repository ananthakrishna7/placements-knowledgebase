import functools

from flask import (
        Blueprint, flash, g, redirect, render_template, request, session, url_for
        )
from werkzeug.security import check_password_hash, generate_password_hash

from sqlalchemy import select, exc

from amrita_place.database import db_session

from amrita_place.models import Administrator

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                new_user = Administrator(username, generate_password_hash(password), name)
                db_session.add(new_user)
                # db_session.execute(text(
                #         "INSERT INTO user (username, password) VALUES (?, ?)"),
                #         (username, generate_password_hash(password)),
                # )
                db_session.commit()
            except:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        # user = db_session.execute(
        #         'SELECT * FROM user WHERE username = ?', (username,)
        #         ).fetchone()
        try:
            user = db_session.execute(select(Administrator).filter_by(username=username)).scalar_one()  
            if not check_password_hash(user.PasswordHash, password):
                error = 'Incorrect password.'      
        except exc.NoResultFound:
            error = 'Incorrrect username.'
        

        if error is None:
            session.clear()
            session['user_id'] = user.AdminID
            return redirect(url_for('landing.index'))

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = db_session.execute(select(Administrator).filter_by(AdminID=user_id)).scalar_one() # there is an error that crops up if we do not logout and then re-initialize the database

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view
