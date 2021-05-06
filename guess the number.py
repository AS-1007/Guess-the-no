import random
print("****Instructions******")
print("You can change the number range in the function till 100")
print("You will have three chances only")
print("Why to wait let us play")
score=0
for num in range(1,4):
    user=input("do you want to change the range Y/N")
    if user=="y":
        x=int(input("enter the number one"))
        print("The second number should be greater than the first number!")
        y=int(input("enter the number two"))
        num=random.randint(x,y)
    else:
        num=random.randint(1,6)
        print("this is system gen",num)
    gusee=int(input("Gusee the number:"))
    if gusee>num:
        print("Its too high")
    elif gusee==num:
        print("Your answrer is correct!")
        if gusee==num:
             score=score+1
        print("Your score is:",score)
    else:
        print("Its too low")
        print(num,"is the computer number")

print("game is over")