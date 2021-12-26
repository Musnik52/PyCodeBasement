from db_config import local_session, create_all_entities
from db_repo import DbRepo
from student import Student
from kita import Kita

create_all_entities()

repo = DbRepo(local_session)

#repo.add_all(classrooms_list := [Kita(floor=1, num_of_students=2, class_avg=95), Kita(floor=2, num_of_students=2, class_avg=90)])
#repo.add_all(students_list := [Student(first_name='avi', last_name='cohen', grade_avg=100, kita_id=1),Student(first_name='benny', last_name='gantz', grade_avg=90, kita_id=1), Student(first_name='gil', last_name='riva', grade_avg=100, kita_id=2), Student(first_name='danny', last_name='sanderson', grade_avg=80, kita_id=2)])
k1 = repo.get_by_id(Kita, 2) #shows students in kita number
print('k1 kita', k1, '\n', k1.students)

repo.update_by_id(Kita, Kita.id, 1, {'class_avg': 100})