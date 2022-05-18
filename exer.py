
# Write a Python code to read an integer in a file e.g 123 and convert it to words e.g
# One hundred and twenty three and
# write the result back to the same file such that your
# file will have "123 One hundred and twenty three " in it
# marksheet= []
# for i in range(0,int(input())):
#     marksheet.append([input(),float(input())])
#     second_lowest = marksheet.sort()

n = int(input("Enter how many times you want to print the list"))
lst = []
for x in range(0, n):
    lst.append([(input()), float(input())])
lst = sorted(lst, key=lambda x: x[1]);
for x in range(1, n):
    if(lst[x][1] != lst[x-1][1]):

        score = lst[x][1]
        break
lst = sorted(lst);
for x in range(n):
    if(lst[x][1] == score):
        print(lst[x][0])