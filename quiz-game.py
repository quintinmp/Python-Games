print("Welcome to my Solar System quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)")
score = 0

answer = input("How many planets are there in our solar system? ")
if answer.lower() == "8": 
    print('Correct! Sorry Pluto')
    score += 1
else:
    print('Incorrect.')

answer = input("Which planet is furthest from Earth in our solar system? ")
if answer.lower() == "neptune": 
    print('Correct. Oh Neptune!')
    score += 1
else:
    print('Incorrect.') 

answer = input("What is the largest planet in our solar system? ")
if answer.lower() == "jupiter": 
    print('Correct. The third brightest object in our sky after venus and the moon.')
    score += 1
else:
    print('Incorrect.')

answer = input("What is the most dense planet in our solar system? ")
if answer.lower() == "earth": 
    print('Correct. Our dense, tiny home Earth.')
    score += 1
else:
    print('Incorrect.')

answer = input("What object do all of the planets orbit around. ")
if answer.lower() == "sun": 
    print('Correct. How heliocentric of you.')
    score += 1
else:
    print('Incorrect.')


if score == 0:
    print("You got no questions correct. Try again please.")
    quit()
else:
    if score == 1:
        print("You got " + str(score) + " question correct")
        print("Thats " + str((score / 5) * 100) + "%.") 
    if score >= 2:
        print("You got " + str(score) + " questions correct!")
        print("Thats " + str((score / 5) * 100) + "%.") 