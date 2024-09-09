import random
from game.combat.utils.StatsSet import StatsSet



class StatsSetFactory:
    def createWithRandomValues():
        statsSet = StatsSet()
        
        statsSet.maxHealthPoints =  random.randint(50, 100)
        statsSet.speedPoints = random.randint(50,100)
        statsSet.attackPoints  = random.randint(50,100)
        statsSet.defensePoints = random.randint(50, 100)



        statsSet.healthPoints = statsSet.maxHealthPoints
        
        return statsSet