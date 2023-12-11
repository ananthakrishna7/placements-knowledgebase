# note: if something doesn't work we amy need to add app.teardown appcontext somethin something

from flask import (
        Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
        )
from werkzeug.exceptions import abort

from amrita_place.auth import login_required
from amrita_place.database import db_session
from amrita_place.models import *
from sqlalchemy import text, select, exc, func# required if we are going to use queries

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')



@bp.route('/profile')
def profile():
    user = db_session.execute(select(Administrator.Name, Administrator.AdminID).where(Administrator.AdminID == 1)).scalar_one()
    return jsonify(user, 1)

@bp.route('/bar')
# @login_required # this causes problems with react. So commenting for now.
def bar(): # this displays company wise placements in the last ten years
    students_aggr = db_session.execute(select(Student.pass_out_year, Company.name, func.count(Student.roll_no).label('count')).join(Company).group_by(Student.companyID)).all()
    data = [] # shall be passed to react
    for year in range(2013, 2023):
            jason = {}
            jason['year'] = year
            data.append(jason)
    for row in students_aggr:
        print(row, row[0])
        for jas in data:
            if jas['year'] == row[0]: # add company count to respective years
                jas[row[1]] = row[2]
    return data
# pie is company composition for current year
@bp.route('/pie')
def pie():
    data = []
    current_comp = db_session.execute(select(Company.name, func.count(Student.roll_no)).join(Company).where(Student.pass_out_year == 2023).group_by(Company.name)).all()
    for row in current_comp:
        data.append({'id':row[0], 'label': row[0], 'value': row[1]}) # id, label, value, color
    return data

@bp.route('/line')
def line():
    pass
    #  student_placements = db_session.execute(select(Student.pass_out_year, Student.branch, func.count(Student.roll_no).label('count')).group_by(Student.branch)).all
    #  data = []
    #  for year in range(2013, 2023):
    #         jason = {}
    #         jason['year'] = year
    #         data.append(jason)
    #  for row in student_placements:
    #     for jas in data:
    #          if jas['year'] == row[0]:
                  

# def process_data(query_result):
#     index = 0 # to number the records
#     data = {} # shall be passed to react
#     # print(students[1][0].roll_no)
#     for row in query_result:
#         print(row, row[0])
#         jason = {'year':row[0], 'company':, 'count':''}
#         # dic.pop('_sa_instance_state', None)
#         data[index] = dic
#         index += 1
#     return data

# def all_student_data():
#     students = db_session.execute(select(Student)).all()
#     data = process_data(students)
#     return data
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
