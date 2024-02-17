# set

my_set={1,2,2,2,3,4}
print(my_set)
print(type(my_set))
print('-'*50)

# adding
my_set.add(5)
print(my_set)
print('-'*50)

# pop
# popped=my_set.pop()
# print(popped)
print('-'*50)

# discard
# iterate
for i in my_set:
    print(i)
print('-'*50)


# set operation
s1={1,2,3,4,5,6}
s2={3,4,5,6,7,8,9}
print('union:', s1|s2)
print('-'*50)

print('intersection:', s1 & s2)
print('-'*50)

print('difference:', s1-s2)
print('difference:', s2-s1)
print('-'*50)

print('symmetric difference:', s1 ^ s2)
print('-'*50)

my_set.clear()
print(my_set)
print('-'*50)



# tuples
tpl=(1,2,2,3,4,5)
print(tpl)
print(tpl[4])
print(tpl[1:3])
print('-'*50)


tpl1=(1,2,3,4,5)
tpl2=(4,5,6,7)
tpl=tpl1+tpl2
print(tpl)
print('-'*50)


for i in tpl:
    print(i)
print('-'*50)

print(tpl*3)









print('-'*50)
