class StatsSet:

    maxHealthPoints = 0;
    healthPoints = 0;
    speedPoints = 0;
    magicPoints = 0;

    attackPoints = 0;
    defensePoints = 0;

    specialAttackPoints = 0;
    specialDefensePoints = 0;

    def create(
            maxHealthPoints = 1,
            speedPoints = 1,
            magicPoints = 1,
            attackPoints = 1,
            defensePoints = 1,
            specialAttackPoints = 1,
            specialDefensePoints = 1
    ):
        statsSet = StatsSet()

        statsSet.maxHealthPoints = statsSet.healthPoints = maxHealthPoints
        statsSet.speedPoints = speedPoints
        statsSet.magicPoints = magicPoints
        statsSet.attackPoints = attackPoints
        statsSet.defensePoints = defensePoints
        statsSet.specialAttackPoints = specialAttackPoints
        statsSet.specialDefensePoints = specialDefensePoints
        
        return statsSet
