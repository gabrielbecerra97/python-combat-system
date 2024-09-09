import random

class Participant:
    def __init__(self, name, statsSet):
        self.__name = name
        self.__statsSet = statsSet
        
    def getName(self):
        return self.__name

    def getStatsSet(self):
        return self.__statsSet

    def getTurnSpeedPoints(self):
        return (self.__statsSet.speedPoints - 3) + random.randint(1, 6)
