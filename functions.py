x=20
def my_function(x): return x + 5
print(x)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana": print(x)
x= 'we are "VIKINGS" of the north.'
x= 'we are \"VIKINGS\" of the north.'
print(x)
'''
x=[1,2,3,4,5,6,7]
for a in x:
 print(a)'''
'''name =['amisha','manisha','mayank']
for names in name:
    print(names*3)
list =['amisha','manisha','mayank','anu']

def loop(x):
    print(x*3)
    loop(list)
num = int(input("entr a number"))
new = num%2
if new>0:
 print("this is an odd number")
else:
 print("this is an even number")

num=int(input('enter a number'))
New = False
if num>1:
    for i in range(2,num):
        if (num%i)==0:
             New = True
             break
if New:
    print("this is not a prime number")
else:
    print("this is a prime number")
nterms = int(input('how many terms'))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
    print("enter a positive number")
elif nterms == 1:
    print(n1)
else:
    print("fibonacci sequence:")
    while count<nterms:
        print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1'''