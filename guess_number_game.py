winning_number = 30

print("Starts Guessing Game")

while True:
    try:
        input_number = int(input("Guess your number 1 to 100"))
        break
    except ValueError:
        print("Please Enter Integer Value!")


guess = 1
game_over = False

while not game_over:

        if winning_number == input_number:
            print(f"You Win the Game!")
            game_over = True


        elif winning_number > input_number:
            print("You Guess Low !")
            guess += 1
            
        try:
            input_number = int(input("Guess Again :"))
        except ValueError:
            print("Please Enter Integer Value!")

        else:
            print("You Guess too High!")
            guess += 1
        try:
            input_number = int(input("Guess Again :"))
        except ValueError:
            print("Please Enter Integer Value!")



'''Shows the platform we are working on'''
# import sys
# print(sys.platform)