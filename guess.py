#numbers guessing game
import random
print(random.randint(1,50))
guess=[]
cpu_num=random.randint(1,50)
player_num=int(input("Enter a number 1 to 50:"))
guess.append(player_num)
while player_num!=cpu_num:
    if player_num>cpu_num:
        print("Too high!!")  
    else:
        print("Too low!!")
    player_num=int(input("Enter a number 1 to 50:"))
    guess.append(player_num)
else:
    print("well done..")
    print("you have taken{} guesses".format(len(guess)))
    print("Here are your guesses:")
    print(guess)