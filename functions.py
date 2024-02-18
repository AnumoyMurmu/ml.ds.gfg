def greet():
    print('hello')

greet()
print('-'*50)

print([greet() for i in range(10)])
print('-'*50)

for i in range(10):
    greet()
print('-'*50)

g_val=2
def greet():
    l_val=5
    print(g_val,l_val)
greet()
print('-'*50)


def greet(n):
    print("hello",n)
greet("anything")  
print('-'*50)


def jog(a,b):
    print(a+b)
jog(12,13) 
print('-'*50)


lst=[1,2,3,4,5]
def sq_lst(lst):
    return [i**2 for i in lst]
def cube_lst(lst):
    return [i**3 for i in lst]

def final(lst):
    ls1=sq_lst(lst)
    ls2=cube_lst(lst)
    return [ls1[i]+ls2[i] for i in range(len(ls1))]

print(sq_lst(lst))
print(cube_lst(lst))
print(final(lst))

 






print('-'*50)
