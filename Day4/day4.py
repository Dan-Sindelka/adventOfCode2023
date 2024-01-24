from re import fullmatch

data = open('Day4/input.txt', 'r').read().split('\n')
testdata = open('Day4/testinput.txt', 'r').read().split('\n')

class MySolution:
    def __init__(self):
        self.finalResult = 0

    # put winning numbers and lot numbers into different lists and then iterate over winnings number to find them in lotnumber
    def logic(self):
        for card in data:
            cardname, results = card.strip().split(":")            
            listOfWinningNumbers, ListOfLotNumbers = results.replace("  ", " ").strip().split("|") # replace to handle additional space in front of single numbers
            curatedWinningNumbers = listOfWinningNumbers.strip().split(" ") # strip needed to delete additional spaces at the end
            curatedLotNumbers = ListOfLotNumbers.strip().split(" ")
            test = 0
            for number in curatedWinningNumbers:
                if number in curatedLotNumbers:
                    test += 1
            if test != 0:
                self.finalResult += 2**(test-1)

class HelpSolution:
    def __init__(self):
        self.finalResult = 0

    # put winning numbers and lot numbers into different sets and use intersection to find number of matching numbers
    def logic(self):
        for card in data:
            cardname, results = card.strip().split(":")            
            listOfWinningNumbers, ListOfLotNumbers = results.replace("  ", " ").strip().split("|") # replace to handle additional space in front of single numbers
            curatedWinningNumbers = set(listOfWinningNumbers.strip().split(" ")) # strip needed to delete additional spaces at the end
            curatedLotNumbers = set(ListOfLotNumbers.strip().split(" ")) #question is if translation to sets is worth it from performace point of view
            test = set.intersection(curatedWinningNumbers,curatedLotNumbers)
            if len(test) != 0:
                self.finalResult += 2**(len(test)-1)

mySolution = MySolution()
mySolution.logic()
print(mySolution.finalResult)

helpSolution = HelpSolution()
helpSolution.logic()
print(helpSolution.finalResult)