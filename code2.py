import random 

dante = random.randint(1,100)
Dnate = int(dante)

while True:
    
    guess = input("Choose a number 1-100 ")
    guess = int(guess)


    if guess > dante:
        print("your number is higer than the answer")

    if guess < dante: 
        print("your number is lower than the answer")

    if guess == dante:
        print("you got the answer congrats")
        break
