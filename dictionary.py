# dictionary

# tel = {1:'Anumoy',2:'bhai', 3:'nope', 1:'anu'}
# tel = {'1':'Anumoy','2':'bhai', '3':'nope', '4':'anu'}

# print(tel)
# print(tel['2'])
# print('bhai' not in tel)
# print(tel.get('1'))
# tel[5]='dawg'
# print(tel[5])
# print(tel)
# del tel['4']
# print(tel)
# tel.clear()
# print(tel)
# <itreating>
# print(tel.keys())
# print(tel.values())

# for i in tel.keys():
#     print(tel[i],':', i)

# print(tel.items())

# for i in tel.items():
#     print(i[0], i[1])

# for i, k in tel.items():
#     print(i, k)

# 

# print('1' in tel)


# # mupdating
tel_1 ={1:'aa',2:'dsc'}
tel_2={3:'sa',4:'d'}
# tel_1.update(tel_2)


# print(tel_1)

print('-'*50)

# multi dimensional dect
md={
     1:{'Name': 'Anumoy', 'Reg': 1519},
      2:{'Name':'Arup', 'Reg': 1520},
      3:{'Name':'Arnab', 'Reg':1521}
}

print(md)
print(md[1])
print(md[1]['Reg'])

print('-'*50)

# updating, deleting

md[1]['Reg']=1518
print(md)

print('-'*50)

md[4]={'Name':'Sudipto', 'Reg':1522}
print(md)

print('-'*50)

del md[4]['Name']
print(md)

print('-'*50)

# iterate

for i in md.keys():
    print(i,':',md[i]['Reg'])




print('-'*50)

# Level up

data={
     1:{'Name': 'Anumoy', 'Reg': 1519, 'Marks': {'Math':22,'Phy':25,'Chem':21}},
      2:{'Name':'Arup', 'Reg': 1520, 'Marks': {'Math':22,'Phy':25,'Chem':21}},
      3:{'Name':'Arnab', 'Reg':1521, 'Marks': {'Math':22,'Phy':25,'Chem':21}}
}

# print(md[1]['Marks'])

for i in data.keys():
    print(i,data[i]['Name'],':',data[i]['Marks'])
    print(i,data[i]['Name'],':',data[i]['Marks']['Math'])


print('-'*50)

#dictionary comprehension

dct={i:i**2 for i in range(1,11)}
print(dct)

print('-'*50)

# dictionary with condition

dct={i:i**2 for i in range(1,11) if i%2==0}
print(dct)

print('-'*50)

dct={'num_'+str(i):i**2 for i in range(1,11) if i%2==0}
print(dct)

print('-'*50)

dck={i for i in range(1,101) if i%3==0}
print(dck)

print('-'*50)

l1=['a','b','c']
l2=[1,2,3]
dckt={l1[i]:l2[i] for i in range(len(l1))}
print(dckt)

print('-'*50)




print('-'*50)





        