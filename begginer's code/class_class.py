import shelve

class Grade():
    def __init__(self, id, subject, student_id, grade):
        self.id = id
        self.subject = subject
        self.student_id = student_id
        self.grade = grade

    def __eq__(self, other):
        if type(other) == int or type(other) == float: return self.grade == other
        if type(self) != type(other): return False

    def __ne__(self):
        return not self.__eq__

    def __add__(self, other):
        if type(other) == int or type(other) == float: return self.grade + other
        if type(self) != type(other): return self.grade

    def __sub__(self, other):
        if type(other) == int or type(other) == float: return self.grade - other
        if type(self) != type(other): return self.grade

    def __mul__(self, other):
        if type(other) == int or type(other) == float: return self.grade * other
        if type(self) != type(other): return self.grade

    def __gt__(self, other):
        if type(other) == int or type(other) == float: return self.grade > other
        if type(self) != type(other): return False

    def __repr__(self):
        return f'Grade: {self.id, self.subject, self.student_id, self.grade}'

    def __str__(self):
        return f'ID: {self.id}\nSubject: {self.subject}\nStudent ID:{self.student_id}\nGrade:{self.grade}'

math = Grade(1, 'math', 308123123, 69 )
spanish = Grade(2, 'spanish', 308123123, 100 )
sport = Grade(3, 'sport', 308123123, 86 )
history = Grade(4, 'history', 308123123, 83 )
list1 = [math, spanish, sport, history]
she = shelve.open('grades.db')
she['1'] = math.__dict__ 
she['2'] = spanish.__dict__ 
she['3'] = sport.__dict__ 
she['4'] = history.__dict__ 
print([she[f'{i}'] for i in she ])
she.close()