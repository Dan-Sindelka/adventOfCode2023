data = open('Day5/input.txt', 'r').read().split('\n\n')
testData = open('Day5/testinput.txt', 'r').read().split('\n\n')

#class with seed as list of numbers
class Master:
    def __init__(self) -> None:
        pass

    #seperate inital seed values, then iterate over instructed operation and then compare if values needs to be changed per instructions
    def mainCycle(self, data):
        seedsname, stringValues = data.pop(0).split(":")
        stringValues = stringValues.strip().split(" ")
        self.values = list(map(int, stringValues))

        for instuction in data:
            name, values = instuction.split(":")
            separatedValues = values.strip().split("\n")
            referenceDictionary = self.changeValuesBasedOnInput(separatedValues)
    
    # by substracting the source value from value itself and then adding the difference to destination value
    def changeValuesBasedOnInput(self, listOfAllValues):
        for value in self.values:      
            for line in listOfAllValues:
                individualValuesAsStr = line.split(" ")
                individualValues = list(map(int, individualValuesAsStr)) # needs ints in list for following math
                destination, source, rangeOfNums = individualValues

                #check if value is in individual ranges and then change it, once changed move to next number
                if 0 <= (dif := value - source) <= rangeOfNums - 1:
                    indexOfValue = self.values.index(value)
                    self.values[indexOfValue] = destination + dif
                    break

master = Master()
master.mainCycle(data)

#take the lowest number
print(min(master.values))





