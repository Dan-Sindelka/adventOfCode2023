import re

data = open('Day6/input.txt', 'r').read().split('\n')
test_data = open('Day6/testinput.txt', 'r').read().split('\n')

class Master:
    def __init__(self):
        self.final_result = 1

    # dict of time(key) and distance(value) / put it as a tuple in list 
    def distribute_data(self, data):
        helperList= []
        for line in data:
            helperList.append(re.findall('\d+', line))
        key_value_pairs = zip(helperList[0], helperList[1])
        self.mainDict = dict(key_value_pairs)

    # iterate through input, and multiply final result with number of ways one can exceed previous record from inpuut   
    def main_action(self):
        for time, distance in self.mainDict.items():
            if (a:= self.fits_criteria(int(time), int(distance))) is not None:
                self.final_result = self.final_result * a
            
    # iterate over half of possible times, the odd one add one every other add 2, and return how many times is the milestone conquered            
    def fits_criteria(self, time, distance):
        better_than_milestone = 0
        for i in range(2, time // 2 + 1):  
            if(i * (time - i) > distance):
                if time % 2 == 0 and i == time // 2:
                    better_than_milestone += 1
                else:
                    better_than_milestone += 2
        return better_than_milestone
            
master = Master()
master.distribute_data(data)
master.main_action()
print(master.final_result)