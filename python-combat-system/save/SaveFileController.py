import json
import os

from game.combat.participants.Participant import Participant
from game.combat.utils.StatsSet import *


class SaveFileController:
    def createNewSaveFile():
        print("No implemented yet")

    def loadCharacter(characterName):
        filePath = os.path.join(os.path.dirname(__file__), "characterSheets", characterName + ".json")
        try:
            with open(filePath, "r") as file:
                jsonData = json.load(file)
                
                statsSet = StatsSet.create(
                        jsonData["max_health_points"],
                        jsonData["speed_points"],
                        jsonData["magic_points"],
                        jsonData["attack_points"],
                        jsonData["defense_points"],
                        jsonData["special_attack_points"],
                        jsonData["special_defense_points"]
                )
                
                participant = Participant(jsonData["name"], statsSet)

                return participant
        except:
            return False
