import random

n = 1
list = ["Snake", "gun ", "water"]
choice = random.choice(list)
print(choice)
a = "Snake"
b = "water"
c = "gun"
you = input("choose a name, a for snake b for water  and c for gun")

if choice == "Snake" and you == "gun":
    print("you won")
elif choice == "Snake" and you == "water":
    print("you loose")
elif choice == "gun" and you == "water":
    print("you won")
elif choice == "gun" and you == "Snake":
    print("you loose")
elif choice == "water" and you == "Snake":
    print("you won")
elif choice == "water" and you == "gun":
    print("you won")
else:
    print("game drop")

