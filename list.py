'''list=['car','bus','bike','cycle']

def loop(x):
    print(x*3)
def map_simple(crazy,items):
    for items in list:
        crazy(items)




map_simple(loop,list)
def my_function(fname, lname): print(lname + " " + fname)
my_function("Coco", "Sheth"
def my_function(food):
    for x in food: print(x)
    fruits = ["apple", "banana", "cherry"]

my_function('fruits')
def my_function(x): return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))'''
list = []
name = int(input("enter the number of elements"))
print("\nEnter names")
for i in range (0,name):
    x = input()
    list.append(x)
print("\nnames are :")
for i in range (0,name):
  print(list[i].capitalize())

