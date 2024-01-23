from re import match

data = open('Day3/input.txt', 'r').read().split('\n')
testdata = open('Day3/testinput.txt', 'r').read().split('\n')


class DataArray:
    def __init__(self):
        self.data = []
        self.arrayOfNumbers = []
        self.arrayOfSpecial = []
        self.finalResult = 0

    def __getArray__(self, indexx, indexy): 
        return self.data[indexx][indexy]

    def getData(self, data): # init array :D
        for line in data:
            self.data.append(list(line))
        self.maxrow = len(self.data)
        self.maxcollum = len(self.data[0])

    def getArrayOfNumbers(self): 
        for row in range(self.maxrow):
            for col in range(self.maxcollum):
                if (self.data[row][col].isnumeric()):
                    self.arrayOfNumbers.append([row, col])        
    
    def succesNeighbor(self, iterator):
        try:
            if (self.arrayOfNumbers[iterator + 1][1] == (self.arrayOfNumbers[iterator][1] + 1)):
                    self.succesNeighbor(iterator + 1)
            else:    
                self.resolvingNumber(iterator, True)
        except IndexError:
            if(len(self.arrayOfNumbers) > 0):
                self.resolvingNumber(iterator, True)
            else:
                print(IndexError)

    def notsuccesNeighbor(self, iterator):
        try:
            if checkNeighbors(dataArray, self.arrayOfNumbers[iterator][0], self.arrayOfNumbers[iterator][1], True) == True:
                self.succesNeighbor(iterator)
            else:
                if (self.arrayOfNumbers[iterator + 1][1] == (self.arrayOfNumbers[iterator][1] + 1)):
                    self.notsuccesNeighbor(iterator + 1)     
                else:
                    self.resolvingNumber(iterator, False)
        except IndexError:
            if(len(self.arrayOfNumbers) > 0):
                self.resolvingNumber(iterator, False)
            else:
                print(IndexError)

    def resolvingNumber(self, iterator, Success):
        helper = []
        for i in range(iterator + 1):
            helper.append(str(self.data[self.arrayOfNumbers[0][0]][self.arrayOfNumbers[0][1]]))
            self.arrayOfNumbers.pop(0)
        if Success:
            self.finalResult += int(''.join(helper))

def checkNeighbors(dataArray, x, y, additional): 
    if additional:
        directions = [(-1, 1), (0, 1), (1, 1)]     
    else:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    for direction in directions:
        dx, dy = direction
        # You should check here that (x+dx, y+dx) 
        # is still inside the matrix
        if (-1 < x + dx < dataArray.maxrow and
            -1 < y + dy < dataArray.maxcollum):
            #other option could be if match("[\d.]", self.data[row][col]) != None:
                #     pass
                # else:    
                #     self.arrayOfSpecial.append(self.data[row][col])
            if match("[@+_=!#$%^&*()<>?\/|}{~:-]", dataArray.__getArray__(dx + x,dy + y)) != None:
                return True
    return False
            
dataArray = DataArray()
dataArray.getData(data)
dataArray.getArrayOfNumbers()
x = 0
while len(dataArray.arrayOfNumbers) > 0: #mayhaps instead of 0 for succ&notsucc send 1?
    if checkNeighbors(dataArray, dataArray.arrayOfNumbers[0][0], dataArray.arrayOfNumbers[0][1], False) == True:
        dataArray.succesNeighbor(0)
    else:
        dataArray.notsuccesNeighbor(0)
print(dataArray.finalResult)