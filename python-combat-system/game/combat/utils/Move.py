from Enum import enum

class Move:
    def __init__(self, name, description, type, points, targetAttribute = 'healthPoints', activeTurns = None):
        self.name = name
        self.description = description
        self.type = type
        self.points =  points
        self.targetAttribute = targetAttribute
        self.activeTurns = activeTurns


class MoveType(Enum):
    ATTACK = 'ATTACK'
    SPECIAL_ATTACK = 'SPECIAL_ATTACK'
    BUFF = 'BUFF'
    DEBUFF = 'DEBUFF'
