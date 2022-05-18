'''dictionary comprehension'''
integer = [0, 1, 2, 3, 4]
binary = ["0","1","10","11","100"]
z = zip(integer,binary)
binary_dic ={ integer:binary for integer, binary in zip(integer,binary)}
print(binary_dic)
'''list comprehension'''
a = [-1,2,3,5,0,-7]
additive_inverse = [i*-1 for i in a ]
print(additive_inverse)
'''set comprehension'''
s = set([1,-1,2,-2,3,-3])
sqr_set = {i*i for i in s}
print(sqr_set)