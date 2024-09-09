import random
def game () :
    game_count = 0
    player_win = 0
    computer_win = 0

    def play_game() :
        nonlocal player_win
        nonlocal computer_win

        your_input = input("\n\nplease enter a number:\n1 : stone\n2 : paper\n3 : scissors\n\n")

        if your_input.lower() == 'quit' :
            return
        if your_input not in ["1","2" , "3"] :
            print("you must enter 1 or 2 or 3")
            return play_game()

        your_choice = int(your_input)
        
        computer_value = random.choice("123")
        computer_choice = int(computer_value)

        def decide_winner (player , computer) :
            nonlocal player_win
            nonlocal computer_win
            print(f"your choice is {player} \ncomputer choice is  {computer}")

            if player == 1 and computer ==3 :
                player_win +=1
                return "you win!"
            elif player == 2 and computer == 3 :
                player_win +=1
                return "you win!"
            elif player == 3 and computer == 2 :
                player_win +=1
                return "you win!"
            elif player == computer :
                return "tie game"
            else :
                computer_win +=1
                return "computer win!"
        
        game_result = decide_winner(your_choice , computer_choice)
        print(game_result)
        nonlocal game_count
        game_count +=1

        print(f"Game count is {game_count} !")
        print(f"player wins {player_win} times")
        print(f"computer wins {computer_win} times")
        return play_game()


    return play_game

play = game()
play()


