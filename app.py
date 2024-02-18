import math

x=10.2
print(math.ceil(x))
print(math.floor(x))
print(math.trunc(x))
print('-'*50)

x=3
print(math.exp(x))
print(math.log10(x))
print('-'*50)

x=90
print(math.sin(x))
print(math.cos(x))
print('-'*50)

print(10, math.factorial(10))
print('-'*50)



# Random
import random
print(random.random())
print(random.randint(1,11))  #random integer between 1 to 11
print(random.choice([1,3,54]))
print(random.random())
print(random.sample([1,2,3,12,6],3))  #list of 3
print(random.uniform(1.0,3.0))  #float with specific range
print('-'*50)



# Date and Time
import datetime
print(datetime.datetime.now())
print(datetime.datetime(2022,10,28,10,30,0))
print(datetime.datetime.now().strftime("%m:%d:%y %H:%M:%S"))   #
# finding out difference
date_1= datetime.datetime(2022,10,28,10,30,0)
date_2=datetime.datetime.now()
print(date_1-date_2)
print('-'*50)



# collections
# unordered map type of // save occurance
from collections import Counter, defaultdict,OrderedDict
lst=[1,1,2,2,2,3,3,3,3,4,4,4,4,4]
print(Counter(lst))
print('-'*50)



# default dictionary
d = defaultdict(int)
d['a']+=2
print(d)
print('-'*50)



# string
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.hexdigits)
print(string.digits)
print(string.octdigits)
print('-'*50)


print(string.punctuation)



















