class Party:
    def __init__(self, name, partyMembers = None):
        if partyMembers is None:
            partyMembers = []

        self.__name = name
        self.__partyMembers = partyMembers

    def getName(self):
        return self.__name

    def getPartyMembers(self):
        return self.__partyMembers
    
    def getActivePartyMembers(self):
        # This function will be change in the future to only return alive party members
        return self.__partyMembers
    
    def setPartyMembers(self, partyMembers):
        self.__partyMembers = partyMembers
        
    def addPartyMember(self, partyMember):
        self.__partyMembers.append(partyMember)
        
    def dumpPartyMembersNames(self):
        print("{}'s party members:".format(self.__name))
        for partyMember in self.__partyMembers:
            print("- {}".format(partyMember.getName()))
    
