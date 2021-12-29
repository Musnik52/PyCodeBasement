import sys
from datetime import datetime
from db_repo import DbRepo
from sqlalchemy import asc, text, desc
from sqlalchemy import text
from students import Student
from teachers import Teacher
from subject import Subject
from lessons import Lesson
from db_config import local_session, create_all_entities

repo = DbRepo(local_session)

repo.delete_table('students')
repo.delete_table('teachers')
repo.delete_table('subjects')
repo.delete_table('lessons')

create_all_entities()

s1 = Student(name = 'danny')
s2 = Student(name = 'boris')
t1 = Teacher(name = 'suzi')
t2 = Teacher(name = 'zipi')
sub1 = Subject(name = 'math' )
sub2 = Subject(name = 'python')
sub3 = Subject(name = 'history')
repo.add_all([s1, s2, t1, t2, sub1, sub2, sub3])
repo.add(Lesson(subject_id=2, teacher_id=2, student_id=1))
repo.add(Lesson(subject_id=3, teacher_id=1, student_id=1))

danny = repo.get_by_condition(Student, lambda query: query.filter(Student.id == 1).first())
print('*'*50)
print(danny.lessons[0].teacher.name)
print('*'*50)
zipi = repo.get_by_condition(Teacher, lambda query: query.filter(Teacher.id == 2).first())
print(zipi.lessons)
print('*'*50)