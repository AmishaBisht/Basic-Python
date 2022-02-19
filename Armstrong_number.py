number = 1634
m = len(str(number))
temp = number
add_sum = 0
while temp!=0:
    #get the last digit in the number
    k = temp%10 
    print( "k", k)
    #find k^m
    add_sum +=k**m 
    print(f"add {add_sum}")
    #floor division 
    #which update number with second last digit as last digit
    temp = temp//10 
    print("temmp", temp)
if add_sum==number:
    print('Armstrong Number in Python')
else:
    print('Not a Armstrong Number in Python')