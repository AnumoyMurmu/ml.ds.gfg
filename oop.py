class person:   #class
    name="anumoy"
    age=23
    

p1=person()   #object
print(p1.name)
print(p1.age)
print('-'*50)


p1.name='udhek'
p1.age=22
print(p1.name)
print(p1.age)
print('-'*50)


class gesture:           #method
    name="anu"

    def greet(self):
        print("hello", self.name)
        return 'hi'

g=gesture()
print(g.greet())
print('-'*50)



class math:
    def factorial(self,n):
        s=1
        for i in range(1,n+1):
            s*=i
        return s

m=math()
print(m.factorial(5))
print('-'*50)





                                                    # METHODS#

class person:

    def __init__(self,name,age):   #it will be created and executed automatically
        print(name)
        print(age)

    def run(self):
        print('run')
        return 1
        
p1=person('khurux',27)        
# print(p1.run())
print('-'*50)




                              #INHERITANCE#

class boss:
    def blow_fire(self):
        print('blow fire')

class meth(boss):
    pass

m=meth()
m.blow_fire()


