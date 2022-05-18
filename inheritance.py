'''class Teacher:
    def Teacher_action(self):
        print("i can teach")

class Engineer:
    def Engineer_action(self):
        print("i can code")

class youtuber:
    def youtuber_action(self):
        print("i make content")

class student(Teacher,Engineer,youtuber):
        pass

c = student()
c.Teacher_action()
c.youtuber_action()
c.Engineer_action()'''

class Animal:
    def __init__(self,habitat):
        self.habitat=habitat

    def print_habitat(self):
        print(self.habitat)

    def Animal_breed(self):
        print("i am a labradore")

class Dog(Animal):
    def __init__(self):
        super().__init__("oscar")
    def love(self):
        print("i love padegree")

c = Dog()
c.print_habitat()
c.love()
