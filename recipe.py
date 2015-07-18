
class Recipe:
    """The recipe is a ser of ingredients which get a MetaGroup number"""
    
    def __init__(self, iNiveau, iIngredientsRecette, iDeadWeight):
        self.__niveau = iNiveau                         # Recipe level (the level belong to MetaGroup level)
        self.__listeIngredRecette = iIngredientsRecette # Ingredients that compose the recipe
        self.__deadWeight = iDeadWeight                 # Weight of ingredients without energetic value
    
    def getRecipeCarbo(self):
        oCarbo = 0
        for aIngredientRecette in self.__listeIngredRecette:
            oCarbo += aIngredientRecette.getCarbo()
        return oCarbo
   
    def getRecipeProteine(self):
        oProteine = 0
        for aIngredientRecette in self.__listeIngredRecette:
            oProteine += aIngredientRecette.getProteine()
        return oProteine
    
    def getRecipeLipide(self):
        oLipide = 0
        for aIngredientRecette in self.__listeIngredRecette:
            oLipide += aIngredientRecette.getLipide()
        return oLipide
    
    def getRecipeFibre(self):
        oFibre = 0
        for aIngredientRecette in self.__listeIngredRecette:
            oFibre += aIngredientRecette.getFibre()
        return oFibre
    
    def getRecipeSodium(self):
        oSodium = 0
        for aIngredientRecette in self.__listeIngredRecette:
            oSodium += aIngredientRecette.getSodium()
        return oSodium
    
    def getRecipeSature(self):
        oSature = 0
        for aIngredientRecette in self.__listeIngredRecette:
            oSature += aIngredientRecette.getSature()
        return oSature
    
    def getRecipeCalories(self):
        oValue = 0
        for aIngredientRecette in self.__listeIngredRecette:
            oValue += aIngredientRecette.getCalories()
        return oValue
    
    def getRecipeWeight(self):
        oValue = self.__deadWeight                              # Add dead weight
        for aIngredientRecette in self.__listeIngredRecette:    # Add ingredients weight
            oValue += aIngredientRecette.getPoids()         
        return oValue
    
    def getNiveau(self):
        return self.__niveau
    
    def __str__(self):
        oValue = str(self.__niveau)
        for aIngredient in self.__listeIngredRecette:
            oValue += "\n" + str(aIngredient)
        return oValue