import pandas
from game.combat.Combat import *

class CombatController:
    """
    CombatController will handle all the combat logic:
    - Contain the parties with the participants
    - Maybe handle debuff?
    - Calculate turns based on participant turns ()
    """
    def __init__(self, combat):
        self.__combat = combat
    
    def beginCombat(participantParties):
        combat = Combat(participantParties)
        return CombatController(combat)
        
    
    def calculateParticipantTurnsOrder(self):
        turnParticipants = []

        for party in self.__combat.getParticipantParties():
            for participant in party.getActivePartyMembers():
                turnParticipants.append({
                    "party": party.getName(),
                    "name": participant.getName(),
                    "speed": participant.getTurnSpeedPoints()
                })
        
        sortedTurnParticipants = sorted_data = sorted(turnParticipants, key=lambda x: x['speed'], reverse=True)

        i = 0
        for turnParticipant in sortedTurnParticipants:
            i += 1
            print("{} - {}'s party member {} speed is : {}".format(i, turnParticipant["party"] ,turnParticipant["name"], turnParticipant['speed']))
            

    