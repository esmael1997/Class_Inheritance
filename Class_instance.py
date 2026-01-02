class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        return(f"Name: {self.name}, Age: {self.age}")
        
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
        
    def displayStudent(self):
        base_info = super().display()
        return f"{base_info}, Major: {self.major}"
    
e1 = Person("Alice", 30)
e2 = Student("Bob", 20, "Computer Science")

print(e1.display())
print(e2.displayStudent())