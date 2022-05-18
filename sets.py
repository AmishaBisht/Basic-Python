'''sets'''
basket = {"oranges", "mango","apple","kiwi","apple","mango"}
print(type(basket))
print(basket)
'''another way to create set'''
a= set()
a.add(1)
a.add(4)
print(a)
'''empty curly brackets are dictionary
it allows list as input'''

num = [1,2,3,4,4,3]
unique_numbers = set(num)
print(unique_numbers)
fs = frozenset(num)
print(fs)
print(a|basket)
print(a<basket)
'''or(|) operent used to add two sets union of two sets , and(&) operator used to intersection, < operator is used to
check the subset 
fs is same as sets but it doesnt allow append or add something'''