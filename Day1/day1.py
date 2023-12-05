from functools import reduce

data = open('Day1/input.txt', 'r').read().split('\n')
inputdata = ['1abc2',
'pqr3stu8vwx',
'a1b2c3d4e5f',
'treb7uchet']

def edit(firstNumber, editNumber):
    numbersInLine = list(filter(lambda char: (char.isdigit()),editNumber))
    finalNumber = numbersInLine[0]+numbersInLine[-1] #create single number from first and last one
    return firstNumber + int(finalNumber)

result = reduce(edit, data, 0)
print(result)