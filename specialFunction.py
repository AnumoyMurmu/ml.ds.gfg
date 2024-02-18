#Zip

lst1=['anu','moy','majhi']
lst2=[32,12,11]
print(list(zip(lst1,lst2)))
print('-'*50)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print([list(row) for row in zip(matrix)])
print([list(row) for row in zip(*matrix)])
print('-'*50)

lst1=[1,2,3]
lst2=[4,5,6]
print([i*j for i,j in zip(lst1,lst2)])
print('-'*50)



#Filter (only true values are taken)
lst=[1,2,3,4,5,6,7,8,9]
def is_even(n):
    return n%2==0
print(list(filter(is_even,lst)))   
print('-'*50)



#Lambda
add_num=lambda x,y:x*y
print(add_num(12,22))
print('-'*50)


num=[1,2,3,4,5,6,7,8,9]
s=filter(lambda x:x%2==0,num)
print(list(s))
print('-'*50)




#Map
num=[1,2,3,4,5,6,7,8,9]
def sqr(x):
    return x**2
print(list(map(sqr,num)))
print('-'*50)



                                #ASCII#

#character to ascii code
#ord
print(ord('A'))
print(ord('1'))
print('-'*50)



#ascii to character
print(chr(65))
print(chr(48))
print('-'*50)

for i in range(33,127):
    print(i,':',chr(i))
print('-'*50)

 
name='anumoy'
for i in name:
    print(i,':',ord(i))