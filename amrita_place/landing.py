# note: if something doesn't work we amy need to add app.teardown appcontext somethin something

from flask import (
        Blueprint, flash, g, redirect, render_template, request, url_for
        )
from werkzeug.exceptions import abort

from amrita_place.auth import login_required
from amrita_place.database import db_session
from sqlalchemy import text # required if we are going to use queries

bp = Blueprint('landing', __name__)

@bp.route('/')
def index():
    # posts = db_session.execute(
    #         'SELECT p.id, title, body, created, author_id, username'
    #         ' FROM post p JOIN user u ON p.author_id = u.id'
    #         ' ORDER BY created DESC'
    #         ).fetchall()
    # return render_template('blog/index.html', posts=posts) # we are giving jinja the posts variable... i think
    return render_template('dashboard/index.html', ) # we are giving jinja the posts variable... i think
