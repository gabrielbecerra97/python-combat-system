import random

from factories.StatsSetFactory import * 
from game.combat.utils.StatsSet import * 
from game.combat.participants.Party import * 
from game.combat.participants.Participant import * 
from game.combat.CombatController import * 
from save.SaveFileController import * 

class CombatWithAttacksTests:

    def run():
        participantNames = [
            'adrian',
            'billy',
            'blanca',
            'gabriel',
            'ichiban',
            'max'
        ]

        random.shuffle(participantNames)

        firstParty = Party('Team #1');
        secondParty = Party('Team #2');

        i = 0;

        for participantName in  participantNames:
         
            partyMember = SaveFileController.loadCharacter(participantName)

            if i < 3:
                firstParty.addPartyMember(partyMember)
            else:
                secondParty.addPartyMember(partyMember)

            i = i + 1


        combatController = CombatController.beginCombat([
            firstParty, secondParty
        ])

        turnNumber = 1

        while 1 < 100:
            print("Turn #" + 1 )
            turnNumber += 1

            orderParticipantList = combatController.calculateParticipantTurnsOrder()
            
            for participant in  orderParticipantList:
                if participant.getStatsSet().healthPoints <= 0:
                    continue
                


