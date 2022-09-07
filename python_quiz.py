print("Hello, Welcome to the Python Quiz Game!")
print("The Python Quiz inludes 10 questions.")

start_game = input("Would you like to play? ")

if start_game.lower() != "yes":
    quit()
print()
print("Okay, Let do this! Good luck!")
print()

score = 0

player_answer = input("Which keyword allows you to load a module? ")

if player_answer.lower() == "import":
    print("CORRECT! Great Job!")
    score += 1
else:
    print("INCORRECT! The correct answer is import")

player_answer = input("Which data structure consists of key value pairs? ")

if player_answer.lower() == "dictionary":
    print("CORRECT! Awesome!")
    score += 1
else:
    print("INCORRECT! The correct answer is dictionary")

player_answer = input("A collection of modules are included in a _______? ")

if player_answer.lower() == "library":
    print("CORRECT! Keep it up!")
    score += 1
else:
    print("INCORRECT! The correct answer is library")


player_answer = input("A function that displays a specified message or string to the screen? ")

if player_answer.lower() == "print":
    print("CORRECT! Great Job!")
    score += 1
else:
    print("INCORRECT! The correct answer is print")


player_answer = input("A function that allows information captured from a user? ")

if player_answer.lower() == "input":
    print("CORRECT! Amazing!")
    score += 1
else:
    print("INCORRECT! The correct answer is input")


player_answer = input("A function used to end a program? ")

if player_answer.lower() == "quit":
    print("CORRECT! Awesome!")
    score += 1
else:
    print("INCORRECT! The correct answer is quit")

player_answer = input("A statement keyword to terminate a loop? ")

if player_answer.lower() == "break":
    print("CORRECT! Great Job!")
    score += 1
else:
    print("INCORRECT! The correct answer is break")

player_answer = input("A statement keyword to skip the remaining code and begin the next iteration? ")

if player_answer.lower() == "continue":
    print("CORRECT! Keep it up!")
    score += 1
else:
    print("INCORRECT! The correct answer is continue")


player_answer = input("A function used to create number sequences? ")

if player_answer.lower() == "range":
    print("CORRECT! Great Job!")
    score += 1
else:
    print("INCORRECT! The correct answer is range")


player_answer = input("If statements are also known as _______statements? ")

print("Last Question")

if player_answer.lower() == "conditional":
    print("CORRECT! Great!")
    score += 1
else:
    print("INCORRECT! The correct answer is conditional")

print()
print("You got " + str(score) + " questions correct!")
print("That's a " + str(score/10 * 100) + "%")
if score >= 90:
    print("Great Job!")
elif score >=70 and score <90:
    print("Not too bad! Room for improvement.")
else:
    print("Study some more and try again later.")
print()
print("Thanks for playing!")
print()