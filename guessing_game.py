class GuessingGame():

    def __init__(self):
        import random
        self.answer_number = random.randint(1,10)
        self.is_solved = False

    def guess(self):
        print(self.answer_number) #prints answer to terminal for debuging
        player_guess = int(input("Guess a number between 1 and 10 "))
        if player_guess < self.answer_number:
            print( f"{player_guess} is too low")
            self.guess()
        elif player_guess > self.answer_number:
            print( f"{player_guess} is too high")
            self.guess()
        else:
            self.is_solved = True
            print( f"{self.answer_number} is correct!")
        

# new_game = GuessingGame()
# new_game.guess()



# needs tdd, comments, cleanup
