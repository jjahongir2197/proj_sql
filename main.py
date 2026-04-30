from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///company.db'

db = SQLAlchemy(app)

class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    deparment_id = db.Column(db.Integer)

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    employee_id = db.Column(db.Integer)

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    project_id = db.Column(db.Integer)

class EmployeeTask(db.Model):
    __tablename__ = 'employee_tasks'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer)
    task_id = db.Column(db.Integer)

if __name__== "__main__":
    with app.app_contaxt
        db.create_all()

    app.run(debug=True)
