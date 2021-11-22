
import random

class ComputerPlayer:
    def list(self, list):
        list = [
            'board',
            'computer',
            'jacket',
            'cold',
            'brown',
            'sweatshirt',
            'tired',
            'phone',
            'notebook',
            'note',
            'sticky',
            'market',
            'hair',]
        return list

    def placeUnderscore(self):
        words = ("variable", "python", "turtle", "string", "loop")
        word = random.choice(words)  # chooses randomly from the choice of words
        print("The word is", len(word), "letters long.")  # used to show how many letters# are in the random word
        displayWord = ""
        letter = ''
        guessed = False
        for letter in word:
            if letter in guessed:
                displayWord +=letter + " "
            else:
                displayWord +="_ "
        print()


