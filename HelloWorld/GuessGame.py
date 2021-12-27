
def guess_function(user_guess,  real_answer):

    global score
    attempt = 0
    is_guessing = True

    while is_guessing and attempt < 3:
        if user_guess == real_answer:

            score = score + 1
            print(score)
            print(f"You are right ! your score is {score}")
            is_guessing = False
        else:
            if attempt < 2:
                user_guess = input("Wrong answer ! try again : ")

            attempt = attempt + 1
            print("Wrong attempt " + str(attempt))

    if attempt == 2:
        print("Sorry that was last attempt")

score = 0
print(" Guess the animal\n")
user_guess = input("Tell the heaviest animal on land : ")
guess_function(user_guess, "a")

user_guess = input("Tell the name a bird: ")
guess_function(user_guess, "b")

user_guess = input("Tell the fastest man: ")
guess_function(user_guess,  "c")
print(" this is your final score " + str(score))
