
a=[3,6,9,12,15]  #List
b=(4,8,12,16,20) #tuple
c={5,10,15,20,25} #set
d={"Name":'Akshika Lakshmi',  #dictionary
   "Age":6,
   "STD":1,
   "Sec":'C'
   }
e='12345' #string

# print('5' in e)
# print (3 in a)
# print (16 in b)
# print (5 in c)

#in statement checks if the value exists in list(collection) or not
#print lists
for x in a:
    print (x)
#print tuple
for y in b:
    print (y)
#print sets
for z in c:
    print(z)
#print strings
for z1 in e:
    print(z1)

#print dictonary(keys and values) is different
for z2 in d.keys():
    print(z2)

for z3 in d.values():
    print(z3)

for key,value in d.items():
    print(key,":",value)
# for z4 in d.items():
#     print (key, '')

#range function
for x in range(5):
    print(x)

for y in range(2,10):
    print(y)

for z in range(1,10,2):
    print(z)
else: #executed once for loops is finished
    print("Finished")




