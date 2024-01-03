data = open('Day2/input.txt', 'r').read().split('\n')

testdata = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

def logic(number, color):
    if (color == "red" and number <= 12):
        return True
    if (color == "green" and number <= 13):
        return True
    if (color == "blue" and number <= 14):
        return True

def isPossible(spacedresults):
    for set in spacedresults:
        spacedsets = set.strip().split(",")
        for cubes in spacedsets:
            spacedcubes = cubes.strip().split(" ")
            if (logic(int(spacedcubes[0]), spacedcubes[1]) != True):
                return False
    return True    


counter = 0

for game in data:
    gamenumber, results = game.strip().split(":")
    spacedresults = results.split(";")
    if (isPossible(spacedresults) == True):
        gamenumber = gamenumber.strip().split(" ")
        counter += int(gamenumber[1])
print(counter)