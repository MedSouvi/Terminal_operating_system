import random


print("|Welcome to the guess Game|")

print("in this game you well guess the random number betwin 0 and 100")

computer_choice = random.randint(0, 100)

while True:
    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("this is not a nomber")
        continue
        
    if computer_choice == choice:
        print("🎉You win ")
        break
    
    elif choice in (computer_choice+1, computer_choice+2, computer_choice+3, computer_choice+4, computer_choice+5, computer_choice+6, computer_choice+7, computer_choice+8, ):
        print("You're very close, it's biggest")


    elif choice in (computer_choice, abs(computer_choice-1), abs(computer_choice-2), abs(computer_choice-3), abs(computer_choice-4), abs(computer_choice-5), abs(computer_choice-6), abs(computer_choice-7), abs(computer_choice-8)): 
        print("You're very close, it's smallest")

    elif choice > computer_choice:
        print("this is so biggest")
    

    elif choice < computer_choice:
        print("this is so smallest")


    if choice > 100 or choice < 0:
        print("this is out the intervall...")
        


