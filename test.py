import random


a = "Who hit the most home runs in the 2010’s"
b = "Who hit the most home runs in the 2000’s"
list = [a, b]


print("Question: ")
q = random.choice(list) 
print(q)

correct = False
while not correct:
    answer = input("Enter answer: ")
    if q == a:
        if answer == "Nelson Cruz":
            correct = True
            print("correct")
        else:
            print("wrong")
            break
    if q == b:
        if answer == "Alex Rodriguz":
            correct = True
            print("correct")
        else:
            print("wrong")
            break



