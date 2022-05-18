# print("Hi, you can perform your calculations here!")
# list1=["add","sub","mul","div"]
# choice=input("You want to use the calculator (yes/no) : ")
# while (True):
#     if choice=="yes":

#         print("calculation starts: ")
#         print("select operation: ")
#         print(list1)
#         cal=input("enter the operation you want to perform : ")

#         num1=float(input("enter a number "))
#         num2=float(input("enter second number "))
#         if(cal=="add"):
#             print(num1, " + ", num2, "is: =", num1+num2)
#         elif(cal=="sub"):
#             print(num1, " - ", num2, "is: =", num1-num2)
#         elif(cal=="mul"):
#             print(num1, " * ", num2, "is: =", num1*num2)
#         elif(cal=="div"):
#             print(num1, " / ", num2, "is: =", num1/num2)
#         next_cal=input("you want to calculate again? (yes/no :")
#         if next_cal=="no":
#             print("Thankyou for using the calculator:)")
#             break
#     else:
#         print("Okay bye:)")
#         break
print("Hi, you can perform your calculations here!")
list1=["add","sub","mul","div"]
choice=input("You want to use the calculator (yes/no) : ")
def addition(num1,num2):
     return num1+num2
def subtraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
def calculation(ope):
    switcher = {
        add:"addition",
        sub:"subtraction",
        mul:"multiplication",
        div:"division",

    }
while (True):
    if choice=="yes":
        print("select operation: ", list1)
        operation=input("Enter the operation you want to perform: ")
        num1=float(input("enter the first digit: "))
        num2=float(input("enter the second digit: "))
        result=switcher.get(ope,lambda:"invalid value")
        print(result)
        next_cal=input("you want to calculate again? (yes/no :")

        if next_cal=="no":
            print("Thankyou for using the calculator:)")
            break
    else:
        print("Okay bye:)")
        break



