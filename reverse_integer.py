
num = int(input("enter the number"))
reverse = 0
while (num>0):
     reminder = num % 10
     reverse = (reverse * 10) + reminder
     num = num // 10
print(f"the reverse of number is {reverse}" )