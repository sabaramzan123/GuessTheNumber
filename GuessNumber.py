import random

def play_game():
    n = random.randint(1, 100)
    a = -1
    guesses = 1

    while a != n:
        a = int(input("Guess the number: "))

        if (a > n):
            print("You are too high\nLower number please")
            guesses += 1
        elif (a < n):
            print("You are too low\nHigher number please")
        guesses += 1
    
    print(f"You have guessed the number {n} correctly in {guesses} attempts")

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break






