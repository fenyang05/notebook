class A():
    name = "haoxiao"
    age = 18
    def say():
        name = "dage"
        print(__class__.age)
        print(A.name)
        return None
p = A()
p.si = 5

print(A.__dict__)
print(p.__dict__)
print(p.si)
A.say()
print(p.name)
print(A.name)