# note: if something doesn't work we amy need to add app.teardown appcontext somethin something

from flask import (
        Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
        )
from werkzeug.exceptions import abort

from amrita_place.auth import login_required
from amrita_place.database import db_session
from amrita_place.models import *
from sqlalchemy import select, exc, func, desc # required if we are going to use queries

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')



@bp.route('/profile')
def profile():
    user = db_session.execute(select(Administrator.Name, Administrator.AdminID).where(Administrator.AdminID == 1)).scalar_one()
    return jsonify(user, 1)

@bp.route('/companies')
def companies():
    data = []
    comps_sal = db_session.execute(select(Company.CompanyID, Company.name, func.max(Student.salary).label('max_salary')).join(Student).group_by(Company.CompanyID)).all()
    for row in comps_sal:
        data.append({'id': row[0], 'name': row[1], 'maxSalary': row[2]})
    return jsonify(data)

@bp.route('/studentData')
def all_student_data():
    students = db_session.execute(select(Student.roll_no, Student.name, Student.email_id, Company.name, Student.salary, Student.CGPA, Student.pass_out_year, Degree.name, Degree.branch).join(Company).join(Degree)).all()
    data = []
    # Process each student record
    for student in students:
        student_data = {
            "id": student[0],
            "name": student[1],
            "email_id": student[2],
            "company_name": student[3],  # Use alias
            "salary": student[4],
            "CGPA": student[5],
            "pass_out_year": student[6],
            "degree_name": student[7],  # Use alias
            "branch": student[8],
        }
        data.append(student_data)
    return jsonify(data)

@bp.route('/companyPlacements')
def all_company_placements(): # CompanyID, COmpanyName, maybe logo??, ASK PRANEETH, No. of students, Avg salary,  order by avg sal,  
    data = []
    comp_place = db_session.execute(select(Company.CompanyID, Company.name, func.count(Student.roll_no), func.avg(Student.salary).label('avg_sal')).join(Student).group_by(Company.CompanyID).order_by(desc('avg_sal'))).all()
    for row in comp_place:
        data.append({'id': row[0], 'name': row[1], 'studentCount': row[2], 'avgSalary': row[3]})
    return jsonify(data)


@bp.route('/create', methods=("POST",))
def create_new_student():
    roll_no = request.json['roll_no']
    name = request.json['name']
    email_id = request.json['email_id']
    linkedIN_profile = request.json['linkedIN_profile']
    salary = request.json['salary']
    cgpa = request.json['CGPA']
    pass_out_year = request.json['pass_out_year']
    companyID = request.json['companyID']
    adminID = request.json['adminID']
    programID = request.json['programID']
    phoneNumber = request.json['phoneNumber']

    student = Student(roll_no=roll_no, name=name, email_id=email_id, linkedIN_profile=linkedIN_profile,
                      salary=salary, CGPA=cgpa, pass_out_year=pass_out_year, companyID=companyID, adminID=adminID, programID=programID)
    phone = PhoneNumber(rollNumber=roll_no, phoneNumber=phoneNumber)
    try:
        db_session.add(student)
        db_session.add(phone)
        db_session.commit()
        return jsonify({'message': 'Student created successfully'}), 201

    except exc.IntegrityError:
        return jsonify({"message": "Primary Key constraint violated"}), 500
    
    except:
        return jsonify({'message':"Error in inserting record"}), 500
    
    


@bp.route('/interviews')
def interviews():
    data = []
    inter = db_session.execute(select(InterviewExperience.interviewID, InterviewExperience.positivePoints, InterviewExperience.improvements, InterviewExperience.isJobSecured, Company.name).select_from(InterviewExperience).join(Company)).all()
    for interview in inter:
        interview_data = {
            "interviewID": interview[0],
            "positivePoints": interview[1],
            "improvements": interview[2],
            "isJobSecured": interview[3],
            "companyName": interview[4],
        }
        data.append(interview_data)
    return jsonify(data)

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

@bp.route('/barCompanies')
def barCompanies():
    data = {'companies': []}
    comp = db_session.execute(select(Company.name))
    for company in comp:
        data['companies'].append(company[0])
    return jsonify(data)

# pie is company composition for current year
@bp.route('/pie')
def pie():
    data = []
    current_comp = db_session.execute(select(Company.name, func.count(Student.roll_no)).join(Company).where(Student.pass_out_year == 2023).group_by(Company.name)).all()
    for row in current_comp:
        data.append({'id':row[0], 'label': row[0], 'value': row[1]}) # id, label, value, color
    return data

@bp.route('/line') # branch wise salary. id and data. id is branch. data {x is year, y is avg_salary}
def line():
    data = [] # NEED TO FINISH THIS
    i = 0
    branches = db_session.execute(select(Degree.programID, Degree.branch)).all()
    for branch in branches:
        data.append({'id': branch[1], 'data': []})
        # this query has to be corrected accoring to the new schema
        branch_sal = db_session.execute(select(Student.pass_out_year, func.avg(Student.salary)).where(Student.programID == branch[0]).group_by(Student.pass_out_year).order_by(Student.pass_out_year)).all()
        for sal in branch_sal:
            data[i]['data'].append({'x': sal[0], 'y': sal[1]})
        i += 1
    return data

    # branch_sal = db_session.execute(select(Student.branch, func.avg(Student.salary), Student.pass_out_year).group_by(Student.branch))
    # for row in branch_sal:
    #     data.append({'id': row[0], 'label': row[0], 'value': row[1]})
    
    #  student_placements = db_session.execute(select(Student.pass_out_year, Student.branch, func.count(Student.roll_no).label('count')).group_by(Student.branch)).all
    #  data = []
    #  for year in range(2013, 2023):
    #         jason = {}
    #         jason['year'] = year
    #         data.append(jason)
    #  for row in student_placements:
    #     for jas in data:
    #          if jas['year'] == row[0]:
                  




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
