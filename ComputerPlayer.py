


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

    def getWord(self,list):
        word = random.choice(list)
        return word.upper()


    def play(self,word):
        word_completion = "_" * len(word)
        print("Let's play Hangman!")
        print(word_completion)
        print("\n")

