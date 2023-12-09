# note: if something doesn't work we amy need to add app.teardown appcontext somethin something

from flask import (
        Blueprint, flash, g, redirect, render_template, request, url_for
        )
from werkzeug.exceptions import abort

from amrita_place.auth import login_required
from amrita_place.database import db_session
from amrita_place.models import *
from sqlalchemy import text, select, exc # required if we are going to use queries

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/profile')
@login_required
def profile():
    return render_template('dashboard/profile.html')

@bp.route('/bar')
# @login_required # idk if this will cause problems with react. So commenting for now.
def bar_data(): # this is like an API
    return all_student_data() 

@bp.route('/pie')
def pie_data():
    return all_student_data()

def all_student_data():
    students = db_session.execute(select(Student)).all()
    index = 0 # to number the records
    data = {} # shall be passed to react
    print(students[1][0].roll_no)
    for student in students:
        stu = student[0].__dict__
        stu.pop('_sa_instance_state')
        data[index] = stu
        index += 1
    return data
# @bp.route('/profile')
# @login_required

# @bp.route('/dashboard')

# @bp.route('/create', methods=('GET', 'POST'))
# @login_required
# def create():
#     if request.method == 'POST':
#         title = request.form['title']
#         body = request.form['body']
#         error = None

#         if not title:
#             error = 'Title is required.'

#         if error is not None:
#             flash(error)
#         else:
#             db = get_db()
#             db.execute(
#                 'INSERT INTO post (title, body, author_id)'
#                 ' VALUES (?, ?, ?)',
#                 (title, body, g.user['id'])                
#             )
#             db.commit()
#             return redirect(url_for('blog.index'))
#     return render_template('blog/create.html')

# def get_post(id, check_author=True):
#     post = get_db().execute(
#             'SELECT p.id, title, body, created, author_id, username'
#             ' FROM post p JOIN user u ON p.author_id = u.id'
#             ' WHERE p.id = ?',
#             (id,)
#             ).fetchone()
#     if post is None:
#         abort(404, f"Post id {id} doesn't exist.")

#     if check_author and post['author_id'] != g.user['id']:
#         abort(403)
    
#     return post

# @bp.route('/<int:id>/update', methods=('GET', 'POST'))
# @login_required
# def update(id):
#     post = get_post(id)

#     if request.method == 'POST':
#         title = request.form['title']
#         body = request.form['body']
#         error = None

#         if not title:
#             error = 'Title is required.'

#         if error is not None:
#             flash(error)
#         else:
#             db = get_db()
#             db.execute(
#                     'UPDATE post SET title = ?, body = ?'
#                     ' WHERE id = ?',
#                     (title, body, id)
#                     )
#             db.commit()
#             return redirect(url_for('blog.index'))

#     return render_template('blog/update.html', post=post)

# @bp.route('/<int:id>/delete', methods=('POST',))
# @login_required
# def delete(id):
#     get_post(id) #here we only need to check if it exists, and if the author is valis, so we don not use the return value 'post'
#     db = get_db()
#     db.execute('DELETE FROM post WHERE id = ?', (id,))
#     db.commit()
#     return redirect(url_for('blog.index'))
