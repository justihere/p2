from numpy import mean, array
import uuid
MAX_SIZE = 20


class Student:
    def __init__(self, name, surname, grades):
        if not isinstance(name, str):
            raise TypeError('Name should be string data type!')
        if not isinstance(surname, str):
            raise TypeError('Surname should be string data type!')
        if not all(isinstance(x, int) for x in grades.values()):
            raise TypeError('Grades values should be int type!')
        if not all(isinstance(x, str) for x in grades.keys()):
            raise TypeError('Grades keys should be string type!')

        self.__name = name
        self.__surname = surname
        self.__id = uuid.uuid4()
        self.__grades = grades

    def __str__(self):
        return f'{self.name} {self.surname}, student id: {self.__id}, average grade: {self.get_average()}'

    def get_average(self):
        return mean(list(self.grades.values()))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name should be string data type!')
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not not isinstance(value, str):
            raise TypeError('Surname should be string data type!')
        self.__surname = value

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, value):
        if not all(isinstance(x, int) for x in value.values()):
            raise TypeError('Grades values should be int type!')
        if not all(isinstance(x, str) for x in value.keys()):
            raise TypeError('Grades keys should be string type!')
        self.__grades = value


class Group:
    def __init__(self):
        self.__student_list = []
        self.__students = 0

    def checker(self, inp):
        return inp.name + inp.surname in [x.name + x.surname for x in self.__student_list]

    def add_student(self, inp):
        if self.__students == MAX_SIZE:
            raise AssertionError('No more than 20 students in a group!')
        if not isinstance(inp, Student):
            raise TypeError('Input should be Student type!')
        if self.checker(inp):
            raise ValueError('Student with this name and surname already exists!')
        self.__student_list.append(inp)
        self.__students += 1

    def top_five(self):
        avg = array([x.get_average() for x in self.__student_list])
        ids = (-avg).argsort()[:5]
        return [self.__student_list[x] for x in ids]

    def __str__(self):
        return '\n'.join([str(x) for x in self.top_five()])


def main():
    a = Student('Kuruch', 'Ivan', {'subj1': 80, 'subj2': 81, 'subj3': 79, 'subj4': 82, 'subj5': 78})
    b = Student('Pylypchyk', 'Mykola', {'subj1': 90, 'subj2': 91, 'subj3': 89, 'subj$': 92, 'subj5': 88})
    c = Student('Dmytro', 'Onoprienko', {'subj1': 75, 'subj2': 76, 'subj3': 74, 'subj4': 77, 'subj5': 73})
    d = Student('Olya', 'Neshcheret', {'subj1': 69, 'subj2': 70, 'subj3': 68, 'subj4': 71, 'subj5': 67})
    e = Student('Kryvytskiy', 'Bohdan', {'subj1': 60, 'subj2': 61, 'subj3': 60, 'subj4': 63, 'subj5': 60})
    f = Student('Kryvokon', 'Agata', {'subj1': 95, 'subj2': 94, 'subj3': 96, 'subj4': 97, 'subj5': 93})
    g = Student('Orhish', 'Iryna', {'subj1': 100, 'subj2': 100, 'subj3': 100, 'subj4': 100, 'subj5': 100})

    group = Group()
    group.add_student(a)
    group.add_student(b)
    group.add_student(c)
    group.add_student(d)
    group.add_student(e)
    group.add_student(f)
    group.add_student(g)

    print(group)


if __name__ == '__main__':
    main()