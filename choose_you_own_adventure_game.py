name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input("You are on a dirt road, it has come to an end, and you can go left or right. Which way would you like to go? : ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. Type walk to walk around and swim to swim across. : ").lower()

    if answer == 'swim':
        print("You swam across and were eaten by an alligator.")
    elif answer == 'walk':
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')


elif answer == "right":
    answer = input("You come to a bridge, it looks unsafe, do you want to cross or head back. Type cross or leave to continue. : ").lower()

    if answer == 'leave':
        print("You head back towards the road but you cannot find it. You are lost.")
    elif answer == 'cross':
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to them (Yes/No)? : ").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win!")
        elif answer == "no":
            print("You ignore the stranger and they attack you. Game Over")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')






else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)