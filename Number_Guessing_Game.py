import random

best_score = None

while 1:
    print("\n Select Difficulty:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Difficult (1-100)")

    choice = int(input("Enter the difficulty (1|2|3) : "))
    if choice == 1:
        low, high = 1, 10
    elif choice == 2:
        low, high = 1, 50
    elif choice == 3:
        low, high = 1, 100
    else:
        print("Invalid Choice! Defaulting to Easy!")
        low, high = 1, 10

    comp_num = random.randint(low,high)
    count = 0
    run = 1

    while run: 
        guess = int(input(f"Enter the guess number (1 to {high}) : "))
        count += 1
        if guess == comp_num:
            print("You guessed it right!")
            run = 0
        elif guess < comp_num:
            print("\t HIGHER NUMBER PLEASE")
        else:
            print("\t LOWER NUMBER PLEASE")

    print(f"Total count attempts : {count}")

    if best_score is None or best_score > count:
        best_score = count
        print("Achieved New High Score!")

    print(f"Best Score is {best_score}")

    check_replay = input("\n Do you want to play again (y/n) : ").lower()
    if check_replay != 'y':
        print("Thanks For Playing!")
        exit()