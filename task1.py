import zope.interface

from zope.interface import implements

class Subject:
    def __init__(self, name: str, duration: int):
        self.__name = name
        self.__duration = duration

    def __str__(self) -> str:
        return '''{} - {} м.'''.format( self.__name, self.__duration)

class Program:
    def __init__(self, name: str, subjects: list):
        self.__name = name
        self.__subjects = subjects
    def __str__(self) -> str:
        return '''Програма: {}\nПерелік тем:\n {}'''.format(self.__name,  '\n'.join([str(subject) for subject in self.__subjects]))   

class ITeacher(zope.interface.Interface):
    pass

@zope.interface.implementer(ITeacher)  
class Teacher:
    def __init__(self, name: str, courses: list):
        self.name = name
        self.__courses = courses

    def __str__(self) -> str:
        return '''{} викладає такі курси:\n{}'''.format(self.name, self.__courses) 

class ICourse(zope.interface.Interface):
    pass

@zope.interface.implementer(ICourse)
class LocalCourse:
    def __init__(self, name: str, teacher: Teacher, program: Program):
        self.__name = name
        self.__teacher = teacher
        self.__program = program

    def __str__(self) -> str:
        return '''Місцевий курс"{}"\n
        Викладач: {}\n
        
        {}'''.format(self.__name, self.__teacher.name, self.__program)

@zope.interface.implementer(ICourse) 
class OffsiteCourse:
    def __init__(self, name: str, teacher: Teacher, program: Program):
        self.__name = name
        self.__teacher = teacher
        self.__program = program

    def __str__(self) -> str:
        return '''Закордонний курс"{}"\n
        Викладач: {}\n
        
        {}'''.format(self.__name, self.__teacher.name, self.__program)

class ICourseFactory(zope.interface.Interface):
    def add_teacher(self, name: str, courses: list):
        pass

    def create_course(self, type: str, name: str, teacher: ITeacher, program: Program):
        pass

@zope.interface.implementer(ICourseFactory)  
class CourseFactory:
    def add_teacher(self, name: str, courses: list):
        return Teacher(name, courses)

    def create_course(self, type: str, name: str, teacher: ITeacher, program: Program):
        if type == 'local':
            return LocalCourse(name, teacher, program)
        elif type == 'offsite':
            return OffsiteCourse(name, teacher, program)
        else:
            raise Exception('Невірний тип')
