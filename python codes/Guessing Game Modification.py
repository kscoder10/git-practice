import random

play_game = True
best_score = None

while play_game:
    lowest_num = int(input("Enter the lowest number: "))
    highest_num = int(input("Enter the highest number: "))
    answer = random.randint(lowest_num, highest_num)

    guesses = 0
    is_running = True

    print(f"Select a number between {lowest_num} and {highest_num}")

    while is_running:

        guess = input("Enter your guess: ")

        if guess.isdigit():
            guess = int(guess)
            guesses += 1

            if guess < lowest_num or guess > highest_num:
                print("Number is out of range")
                print(f"Please select a number between {lowest_num} and {highest_num}")

            elif guess < answer:
                print("Too Low! Try again")

            elif guess > answer:
                print("Too High! Try again")

            else:
                print(f"Congratulations it is correct! The answer was {answer}")
                print(f"Number of guesses: {guesses}")

                if best_score is None or guesses < best_score:
                    best_score = guesses

                print(f"Best score: {best_score}")
                play_game = False
                is_running = False


        else:
            print("Invalid guess")
            print(f"Please select a number between {lowest_num} and {highest_num}")

        if guesses >= 7 and is_running:
            print("Sorry, you have reached a maximum of seven attempts!")
            is_running = False

            play_again = input("Do you want to play again? (y/n): ")

            if play_again == "y":
                play_game = True

            elif play_again == "n":
                play_game = False
                play_game = False
                print("Game over!")
