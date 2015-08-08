from portions import PortionGroup
from exception import MyException
from constants import Constants


class MetaGroup(object):
    """This class classifies ingredients in 4 levels """
    
    def __init__(self, iNiveau, iCalories):
        self.__niveau = iNiveau     # Level of the MetaGroup
        self.__calories = iCalories # Total of calories defined in the MetaGroup
        self.__groups = []          # Set of all groups linked to one MetaGroup
        self.__configGroups()       # Initialization of groups
    
    def __configGroups(self):
        """Configure all groups of one MetaGroup according to the documentation"""
        
        if self.niveau == 1 :
            self.__groups.append(Group(1, Constants.DescPortionGrp1, Constants.NbPortionGrp1))
        elif self.niveau == 2 :
            self.__groups.append(Group(2, Constants.DescPortionGrp2, Constants.NbPortionGrp2))
            self.__groups.append(Group(3, Constants.DescPortionGrp3, Constants.NbPortionGrp3))
        elif self.niveau == 3 :
            self.__groups.append(Group(4, Constants.DescPortionGrp4, Constants.NbPortionGrp4))
            self.__groups.append(Group(5, Constants.DescPortionGrp5, Constants.NbPortionGrp5))
        elif self.niveau == 4 :
            self.__groups.append(Group(6, Constants.DescPortionGrp6, Constants.NbPortionGrp6))
            self.__groups.append(Group(7, Constants.DescPortionGrp7, Constants.NbPortionGrp7))
        else:
            raise MyException("__configGroups() : Nivel de sobre group errado, escolhe em {1, 2, 3, 4}")
    
    def __str__(self):
        oValue = str(self.niveau) + " " + str(self.calories)
        for aGroup in self.__groups:
            oValue += " " + str(aGroup) + " "
        return oValue
    
    def getGroups(self):
        return self.__groups
    
    def getNiveau(self):
        return self.__niveau
    
    def getCalories(self):
        return self.__calories
    
    niveau = property(getNiveau, "niveau doc")
    calories = property (getCalories, "calories doc")
        
        
class Group:
    """This class classifies ingredients in 7 levels, it is linked to the MetaGroup Class"""
    
    def __init__(self, iNum, iDesc, iNbPortion):
        self.__numero = iNum                    # Number of the group
        self.__description = iDesc              # Short description of group's ingredients
        self.__nbPortion = iNbPortion           # Number of protion in one group
        self.__portion = self.__configPortion() # Portion object in one group
        
    def getPortionCalories(self):
        return self.__portion.getCalories()
    
    def getNumber(self):
        return self.__numero
    
    def getDesc(self):
        return self.__description
        
    def __configPortion(self):
        """Configuration of portions in each group"""
        if self.__numero == 1 :
            return PortionGroup(Constants.CaloriePortionGrp1)
        elif self.__numero == 2 :
            return PortionGroup(Constants.CaloriePortionGrp2)
        elif self.__numero == 3 :
            return PortionGroup(Constants.CaloriePortionGrp3)
        elif self.__numero == 4 :
            return PortionGroup(Constants.CaloriePortionGrp4)
        elif self.__numero == 5:
            return PortionGroup(Constants.CaloriePortionGrp5)
        elif self.__numero == 6 :
            return PortionGroup(Constants.CaloriePortionGrp6)
        elif self.__numero == 7 :
            return PortionGroup(Constants.CaloriePortionGrp7)
        else:
            raise MyException("__configPortion() : Numero de groupo errado, escolhe em {1, 2, 3, 4, 5, 6, 7}")
    
    def __str__(self):
        oValue = str(self.__numero) + " "
        oValue += str(self.__nbPortion) + " " + str(self.__portion)
        return oValue