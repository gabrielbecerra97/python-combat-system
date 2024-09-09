import random

from factories.StatsSetFactory import *
from game.combat.utils.StatsSet import *
from game.combat.participants.Party import *
from game.combat.participants.Participant import *
from game.combat.CombatController import *

participantNames = [
    'Gabriel',
    'Adrian',
    'Blanca',
    'Max',
    'Fer',
    'Billy'
]

random.shuffle(participantNames)

firstParty = Party('Chadz');
secondParty = Party('ZZZ');

i = 0;

for participantName in  participantNames:
 
    statsSet = StatsSetFactory.createWithRandomValues();
    partyMember = Participant(participantName, statsSet)


    if i < 3:
        firstParty.addPartyMember(partyMember)
    else:
        secondParty.addPartyMember(partyMember)

    i = i + 1


combatController = CombatController.beginCombat([
    firstParty, secondParty
])

combatController.calculateParticipantTurnsOrder()