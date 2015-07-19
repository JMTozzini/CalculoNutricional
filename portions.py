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
        oStr = "Groupo: " + str(self.__getGroup().getNumber()) + ", " + self.__getGroup().getDesc() +".\n"
        oStr += "Peso de uma porcao: " + str("%.3f" % self.getPoids()) + " g.\n"
        oStr += "Carbo: \t\t" + str("%7.3f" % self.__carbo) + " g \t" + str("%5.2f" % float(self.__carbo/Constants.CarboJour*100)) + "%\n"
        oStr += "Proteina: \t" + str("%7.3f" % self.__proteine) + " g \t" + str("%5.2f" % float(self.__proteine/Constants.ProteineJour*100)) + "%\n"
        oStr += "Lipideos: \t" + str("%7.3f" % self.__lipide) + " g \t" + str("%5.2f" % float(self.__lipide/Constants.LipideJour*100)) + "%\n"
        oStr += "Fibra: \t\t" + str("%7.3f" % self.__fibre) + " g \t" + str("%5.2f" % float(self.__fibre/Constants.FibreJour*100)) + "%\n"
        oStr += "Sodio: \t\t" + str("%7.3f" % self.__sodium) + " mg \t" + str("%5.2f" % float(self.__sodium/Constants.SodioJour*100)) + "%\n"
        oStr += "Saturados: \t" + str("%7.3f" % self.__sature) + " g \t" + str("%5.2f" % float(self.__sature/Constants.SatureJour*100)) + "%\n"
        return oStr