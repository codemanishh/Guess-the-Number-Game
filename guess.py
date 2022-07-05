import random

number=random.randint(1,100)
user_guess=int(input("hay Guess the nuber : "))
attempt=1
while(True):
    if user_guess>number :
        user_guess=int(input("Hay, Guess another number, this Number is too big "))
        attempt+=1

    elif number>user_guess :
        user_guess=int(input("Hay, Guess another number, this Number is too less "))
        attempt+=1
    else:
        print(f"yahh, you guessed the correct number in {attempt} attemps👨‍💻")
        break

