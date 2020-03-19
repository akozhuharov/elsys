class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __add__(self, other_obj):
        return self.age + other_obj.age

    def __sub__(self, other_obj):
        return self.age - other_obj.age
    
    def __mul__(self, other_obj):
        return self.age * other_obj.age
    
    def __radd__(self, age):
        print(age)
        return self.age + age


p1 = Person("Goshko", 15)
p2 = Person("Ivan", 14)
print(p2 * p1)
