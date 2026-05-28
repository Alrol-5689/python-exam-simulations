from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

class Student(User):
    def __init__(self, name, age, notes):
        super().__init__(name, age)
        self.notes = notes

    def get_notes(self):
        return self.notes
    

class Main():
    Student1 = Student("Juan", 20, [10, 9, 8])
    print(Student1.get_notes())

    
if __name__ == "__main__":
    Main()
