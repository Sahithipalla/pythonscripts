import random 
print("""winning rules:\n
      "rock vs paper => paper wins"\n
      "rock vs scissor => rock wins"\n
      "paper vs scissor => scissor wins"\n""")
#condition for user
while True:
    print("enter choice 1:rock,2:paper,3:scissor")
    user_choice=int(input("user turn:"))
    while user_choice>3 or user_choice<1:
        user_choice=int(input("enter valid input:"))
    if user_choice=="1":
        user_choice_name="rock"
    elif user_choice=="2":
        user_choice_name="paper"
    else:
        user_choice_name="scissor"
    print("user_choice is: "+ user_choice_name)
    print("\n It's computer's turn:") 
#condition for computer
    comp_choice=random.randint(1,3)
    while comp_choice==user_choice:
        comp_choice=random.randint(1,3)
    if comp_choice=="1":
        comp_choice_name="rock"
    elif comp_choice=="2":
        comp_choice_name="paper"
    else:
        comp_choice_name="scissor"
    print("computer's choice is a :"+comp_choice_name)
    print(user_choice_name +"v/s" + comp_choice_name)
#condition for winning
    if ((user_choice==1 & comp_choice==2) or (user_choice==2 & comp_choice==1)):
        print("paper wins=>", end="")
        result="paper"

    elif ((user_choice==1 & comp_choice==3) or (user_choice==3 & comp_choice==1)):
        print("rock wins=>", end="")
        result="rock"
    else:
        print("scissor wins=.", end="")
        result="scissor"
#pinting the winner
    if result==user_choice_name:
        print("<** user wins **>")
    else:
        print("<** computer wins **>")
    print("do you want to play again?(Y/N)" )
    ans=input()
#if user input n or N then break
    if ans=="n" or ans=="N":
        break
print("\n Thanks for playing")
       