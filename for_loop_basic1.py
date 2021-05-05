#1
for x in range(151):
    print(x)
#2
for x in range(5,1001,5):
    print(x)
#3
for x in range(1,101):
    if x % 10 == 0: 
        print ("Coding Dojo")
    elif x % 5 == 0: 
        print ("Coding")
    else:
        print (x)
y = 0
#4
for x in range(1,500000,2):
    y = y + x
print (y)
#5
for x in range(2018,0,-4):
    print (x)
#6
lowNum = 1
highNum = 100
mult = 7
for x in range(lowNum,highNum):
    if x % mult == 0:
        print(x)