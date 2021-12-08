class Grade:

    grade_i = 0
    grade_sum = 0

    def __init__(self, name, grade, topic):
        Grade.grade_i += 1
        self.grade_i = Grade.grade_i
        self.__name = name
        self.__grade = grade
        Grade.grade_sum += grade
        self.__topic = topic
    
    @property
    def grade(self):
        return f'#{self.__grade}#'

    @grade.setter
    def grade(self,new_grade):
        if new_grade > 100 or new_grade < 0:
            print('Invalid grade!')
            return
        self.__grade = new_grade

    @property
    def name(self):
        return f'*{self.__name}*'

    @property
    def topic(self):
        return f'=-{self.__topic}-='
    
    @topic.setter
    def topic(self, new_topic):
        l = ['english', 'python', 'math']
        if new_topic not in l:
            print('invalid!')
            return
        self.__topic = new_topic
    
    @staticmethod
    def get_grade_i():
        return Grade.grade_i

    @staticmethod
    def get_avg():
        return Grade.grade_sum / Grade.grade_i

    def is_grade_higher_than_avg(self):
        return f'Grade higher than average' if self.__grade > (Grade.grade_sum / Grade.grade_i) else f'Grade smaller than average'

    def __repr__(self):
        return f'Grade: ({self.grade_i}, {self.__name}, {self.__grade}, {self.__topic})'
    
    def __str__(self):
        return f'Grade: Index: {self.grade_i}, Name: {self.__name}, Grade: {self.__grade}, Topic: {self.__topic})'