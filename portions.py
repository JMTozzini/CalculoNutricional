from constants import Constants


class PortionGroup:
    """Each group is divided in egual portions"""
    
    def __init__(self, iCal):
        self.__calories = iCal  # Calory of one portion
    
    def getCalories(self):
        return self.__calories
    
    def __str__(self):
        oValue = str(self.__calories)
        return oValue
        
        
class PortionRecette:
    """Each recipe return a determined portion"""
    
    def __init__(self, iPoids, iGroup, iCarbo, iProteine, iLipide, iFibre, iSodium, iSature):
        self.__poids = iPoids       # Weight of one recipe portion
        self.__group = iGroup       # Group of one recipe portion
        self.__carbo = iCarbo       # Carbo of one recipe portion
        self.__proteine = iProteine # Proteine of one recipe portion
        self.__lipide = iLipide     # Lipide of one recipe portion
        self.__fibre = iFibre       # Fibre of one recipe portion
        self.__sodium  = iSodium    # Sodium of one recipe portion
        self.__sature = iSature     # Saturated grease of one recipe portion
        
    def getPoids(self):
        return self.__poids
    
    def __getGroup(self):
        return self.__group
    
    def __str__(self):
        oValue = "Groupo: " + str(self.__getGroup().getNumber()) + ", " + self.__getGroup().getDesc() +".\n"
        oValue += "Peso de uma porcao: " + str("%.3f" % self.getPoids()) + " g.\n"
        oValue += "Carbo: " + str("%.3f" % self.__carbo) + " g, " + str("%.2f" % float(self.__carbo/Constants.CarboJour*100)) + "%\n"
        oValue += "Proteina: " + str("%.3f" % self.__proteine) + " g, " + str("%.2f" % float(self.__proteine/Constants.ProteineJour*100)) + "%\n"
        oValue += "Lipideos: " + str("%.3f" % self.__lipide) + " g, " + str("%.2f" % float(self.__lipide/Constants.LipideJour*100)) + "%\n"
        oValue += "Fibra: " + str("%.3f" % self.__fibre) + " g, " + str("%.2f" % float(self.__fibre/Constants.FibreJour*100)) + "%\n"
        oValue += "Sodio: " + str("%.3f" % self.__sodium) + " mg, " + str("%.2f" % float(self.__sodium/Constants.SodioJour*100)) + "%\n"
        oValue += "Saturados: " + str("%.3f" % self.__sature) + " g, " + str("%.2f" % float(self.__sature/Constants.SatureJour*100)) + "%\n"
        return oValue