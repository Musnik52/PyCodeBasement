from person import Person
from grade import Grade

boris = Person(1, 'Boris', 29)
math = Grade(boris.name, 89, 'math')
python = Grade(boris.name, 100, 'python' )


print(boris)
print(boris.age)
print(boris.name)
boris.name = 'bar'
print(boris.name)
boris.name = 'Baruch'
print(boris.name)
print('*'*50)
print(python)
print(math.get_avg())
print(python.topic)
print(math.is_grade_higher_than_avg())

