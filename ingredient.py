class Ingredient(object):
    """All data concerning an ingredient, it's copy of Excel ingredient"""
    
    def __init__(self):
        self.__nom = ""
        self.__numero = 0
        self.__calories = 0
        self.__carbo = 0
        self.__proteine = 0
        self.__lipide = 0
        self.__fibre = 0
        self.__sodium  = 0
        self.__sature = 0

    def __str__(self):
        oValue = "nom " + self.nom
        oValue += " numero " + str(self.numero)
        oValue += " calories " + str(self.calories)
        oValue += " carbo " + str(self.carbo)
        oValue += " proteine " + str(self.proteine)
        oValue += " lipide " + str(self.lipide)
        oValue += " fibre " + str(self.fibre)
        oValue += " sodium " + str(self.sodium)
        oValue += " sature " + str(self.sature)
        return oValue

    def get_nom(self):
        return self.__nom

    def get_numero(self):
        return self.__numero

    def get_calories(self):
        return self.__calories

    def get_carbo(self):
        return self.__carbo

    def get_proteine(self):
        return self.__proteine

    def get_lipide(self):
        return self.__lipide

    def get_fibre(self):
        return self.__fibre

    def get_sodium(self):
        return self.__sodium
    
    def get_sature(self):
        return self.__sature

    def convertToFloat(self, ioValue):
        try : ioValue = float(ioValue)
        except: ioValue=0
        return ioValue   

    def set_nom(self, value):
        self.__nom = value

    def set_numero(self, value):
        value = int(float(value))
        self.__numero = value

    def set_calories(self, value):
        self.__calories = self.convertToFloat(value)

    def set_carbo(self, value):
        self.__carbo = self.convertToFloat(value)

    def set_proteine(self, value):
        self.__proteine = self.convertToFloat(value)

    def set_lipide(self, value):
        self.__lipide = self.convertToFloat(value)

    def set_fibre(self, value):
        self.__fibre = self.convertToFloat(value)

    def set_sodium(self, value):
        self.__sodium = self.convertToFloat(value)
        
    def set_sature(self, value):
        self.__sature = self.convertToFloat(value)
    
    
    nom = property(get_nom, set_nom, "nom's docstring")
    numero = property(get_numero, set_numero, "numero's docstring")
    calories = property(get_calories, set_calories, "calories' docstring")
    carbo = property(get_carbo, set_carbo, "carbo's docstring")
    proteine = property(get_proteine, set_proteine, "proteine's docstring")
    lipide = property(get_lipide, set_lipide, "lipide's docstring")
    fibre = property(get_fibre, set_fibre, "fibre's docstring")
    sodium = property(get_sodium, set_sodium, "sodium's docstring")
    sature = property(get_sature, set_sature, "sature's docstring")


class IngredientRecette:
    """Represente the ingredient used in one recipe"""
    
    def __init__(self, iPoids, iIngredient):
        self.__poids = iPoids           # Weight of one ingredient in one recipe
        self.__ingredient = iIngredient # Ingredient concerned
    
    def getCarbo(self):
        return (self.__ingredient.carbo * self.getPoids())/100
    
    def getProteine(self):
        return (self.__ingredient.proteine * self.getPoids())/100 
    
    def getLipide(self):
        return (self.__ingredient.lipide * self.getPoids())/100
    
    def getFibre(self):
        return (self.__ingredient.fibre * self.getPoids())/100 
    
    def getSodium(self):
        return (self.__ingredient.sodium * self.getPoids())/100 
    
    def getSature(self):
        return (self.__ingredient.sature * self.getPoids())/100 
    
    def getCalories(self):
        return (self.__ingredient.calories * self.__poids)/100
    
    def getPoids(self):
        return self.__poids
    
    def __str__(self):
        oValue = str(self.__ingredient.numero) + " " + str(self.__poids) + " " + str(self.getCalories())
        return oValue