#write a while loop
while True:
    #write code to prompt the user to enter 'rock', 'paper', or 'scissors' and store the input in a variable called user_choice.then print out the user's choice.
    user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
    print(user_choice)
    #write code to generate a random choice from (rock, paper, scissors) and store the input in a variable called computer_choice. then print out the computer's choice.
    import random
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(computer_choice)
    #write code to compare the user_choice and computer_choice using nested if statements. then print out the result of the game.
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    else:
        print("I don't understand that! Please enter rock, paper, or scissors and try again.")
    #write code to prompt the user to play again. if the user chooses 'yes', restart the game, otherwise exit the game.
    play_again = input("Play again? Enter Yes or No: ")

    if play_again.lower() != "yes":
        print("Thanks for playing! Come back soon!")
        exit()
