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
        return (self.__statsSet.speedPoints - 10) + random.randint(0, 20)

    def dumpCharacterSheet(self):
        print("""Character: {}

            - Max HP: {}
            - Speed: {}
            - Magic: {}
            - Attack: {}
            - Defense: {}
            - Special Attack: {}
            - Special Defense: {}
        """.format(
            self.__name,
            self.__statsSet.maxHealthPoints,
            self.__statsSet.speedPoints,
            self.__statsSet.magicPoints,
            self.__statsSet.attackPoints,
            self.__statsSet.defensePoints,
            self.__statsSet.specialAttackPoints,
            self.__statsSet.specialDefensePoints,
        ))