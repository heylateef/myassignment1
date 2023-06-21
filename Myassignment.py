# Q1. Create one variable containing following type of data:
var1="Syed Rahman ur Lateef"
var2=["Lateef",20,30,60,90]
var3='Lateef',[10,30,40],10.6,(30,40,50,70)
print(var3)
print(type(var3))
#Q2. Given are some following variables containing data:
var4 = ' '
var5 = '[ DS , ML , Python]'
var6 = [ 'DS','Ml','Python' ]
var7 = 1.
#What will be the data type of the above given variable.
#ans
print(type(var4))
print(type(var5))
print(type(var6))
print(type(var7))
# Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
# element and its data type.
l=[10,30,"Lateef",6.23,50,60,True,90.5,"Rahman"]
for i in l :
    print(type(i))
for i in l:
    print(i)
# Create a list containing 25 int type data. Using for loop and if-else condition print if the element is divisible by 3 or not.
list=[60,70,3,10,9,15,33,90,100,6,9,4,8,10,14,18,5,25,30,105,111,22]
for i in list:
    if i % 3 ==0:
        print(i)