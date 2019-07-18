# python中任何类都有一个父类叫object
class person():
    name = "haoxiao"
    age = 18
    def selp(self):
        print("I am sleeping......")

class teach(person):
    pass

t = teach()
print(t.name)
print(teach.age)
