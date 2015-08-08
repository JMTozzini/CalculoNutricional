from data import Data
from groups import MetaGroup
from exception import MyException
from constants import Constants
from portions import PortionRecette


class Model(object):
	"""Model of the application, it contains the main information"""

	def __init__(self):
		self.__data = Data();                       # Ingredient Data class used to import and load data
		self.__recette = 0                          # Last recipe specified
		self.__metaGroups = []                      # All groups datas
		self.__initDatas()                          # Iniciate groups datas
		
	def __initDatas(self):
		"""Create all groups rules explicated in the documentation"""
		self.__metaGroups.append(MetaGroup(1, Constants.CalorieMetaGroup1))
		self.__metaGroups.append(MetaGroup(2, Constants.CalorieMetaGroup2))
		self.__metaGroups.append(MetaGroup(3, Constants.CalorieMetaGroup3))
		self.__metaGroups.append(MetaGroup(4, Constants.CalorieMetaGroup4)) 

	def calculatePortions(self):
		"""Calculate one portion of one recipe"""
		aMetaGroup = self.__getMetaGroup(self.recette.getNiveau())
		aGroups = aMetaGroup.getGroups()
		oPortionList = []
		for aGroup in aGroups :
			aPoidsPortion = (self.recette.getRecipeWeight() * aGroup.getPortionCalories())/self.recette.getRecipeCalories()
			aCarbo = (self.recette.getRecipeCarbo() * aPoidsPortion)/self.recette.getRecipeWeight()
			aProteine = (self.recette.getRecipeProteine() * aPoidsPortion)/self.recette.getRecipeWeight()
			aLipide = (self.recette.getRecipeLipide() * aPoidsPortion)/self.recette.getRecipeWeight()
			aFibre = (self.recette.getRecipeFibre() * aPoidsPortion)/self.recette.getRecipeWeight()
			aSodium = (self.recette.getRecipeSodium() * aPoidsPortion)/self.recette.getRecipeWeight()
			aSature = (self.recette.getRecipeSature() * aPoidsPortion)/self.recette.getRecipeWeight()
			oPortionList.append(PortionRecette(aPoidsPortion, aGroup, aCarbo, aProteine, aLipide, aFibre, aSodium, aSature))
		return oPortionList       

	def __getMetaGroup(self, iNiveau):
		for oMetaGroup in self.__metaGroups:
			if oMetaGroup.getNiveau() == iNiveau:
				return oMetaGroup
		raise MyException("getMetaGroup() : Nivel de sobre grupo errado.")

	def checkNumIngr(self, iNumero): 
		"""Check if the ingredient is in the ingredients list"""
		for aIngredient in self.__data.getIngredients():
			if aIngredient.numero == iNumero:
				return True
		return False

	def displayModel(self):
		"""Display all the model"""
		for aMetaGroup in self.__metaGroups:
			print(aMetaGroup)
			
	def displayRecipe(self):
		"""Display the recipe"""
		print(self.recette)

	def resetDatabase(self):
		"""Reset the database and load from the Excel file."""
		self.__data.resetData()
		
	def getIngredient(self, iNumero):
		"""Retrieve the ingredient thanks to the ingredient number"""
		for oIngredient in self.__data.getIngredients():
			if oIngredient.numero == iNumero:
				return oIngredient
		raise MyException("getIngredient() : Numero de ingrediente errado.")

	def getIngredients(self):
		"""Retrieve all ingredients"""
		return self.__data.getIngredients()

	def setRecette(self, iRecette):
		self.__recette = iRecette
		
	def getRecette(self):
		return self.__recette

	recette = property(getRecette, setRecette, "Recette doc")
