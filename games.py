import random
_random = random.randint(0,10) #choose your number under 10
chance = 5
chances_left = 0
print("\t\t\t\t\t\t........This is choice numbers game........")

start_game = print("1 - Start Game")
_read = print("2 - Read Terms And Conditions On Game")
enter_choice = int(input("Enter Choice Here : \n"))
if enter_choice == 1:
    while chances_left < chance:
        game_start = int(input("Choose Under 10 minimum number: "))

        if game_start and _random:
            print(f"you have choose {game_start}")
            if game_start == _random:
                print("Congrats, You Win the Game Sir")
                break
            else:
                print("Wrong Number, Please Try again")

        elif game_start and _random:
            print(f"You have choose {game_start}")
            if game_start == _random:
                print("Congrats, You Win the Game Sir")
                break
            else:
                print("Wrong Number, Please Try again")
        elif game_start and _random:
            print(f"you have choose {game_start}")
            if game_start == _random:
                print("Congrats, You Win the Game Sir")
                break
            else:
                print("Wrong Number, Please Try again")
        elif game_start and _random:
            print(f"you have choose {game_start}")
            if game_start == _random:
                print("\t\tCongrats, You Win the Game Sir")
                break
            else:
                print("Wrong Number, Please Try again")
        elif game_start and _random:
            print(f"You have choose {game_start}")
            if game_start == _random:
                print("\t\tyou Win")
                break
            else:
                print("You Lose this Game Sir..")

        chances_left = chances_left + 1
        print(f"\t\t\t\t\t\tyou have left {chance - chances_left} of {chance}..")
    print(f"\t\t\t\t\t\t\t\t\tThe Computer Random Number is {_random}")

else:
    print("(1) - You can choice Number under 10 minimum....\n")
    print("(2) - you Have minimum 5 chances left only.. \n")



