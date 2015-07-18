#! /usr/bin/python

import xlrd, pickle
from ingredient import Ingredient

class Data :
	"""Class used to import Excel data"""
	
	def __init__(self):
		self.__DataFilePath = "./media/Taco_4a_edicao_2011.xls"		# Data file path of the Excel file
		self.__excelFile = xlrd.open_workbook(self.__DataFilePath)	# Object that opens and contains the Excel file
		self.__sheetNutriments = self.__excelFile.sheet_by_index(0)	# Nutriment sheet
		self.__sheetGrease = self.__excelFile.sheet_by_index(1)		# Grease sheet
		self.__valuesColsNutriments = {								# Nutriment columns numbers
			"numero":	0,
			"nom":		1,
			"calories":	3,
			"carbo":	8,
			"proteine":	5,
			"lipide":	6,
			"fibre":	9,
			"sodium":	17			
			}
		self.__valuesColsGrease = {		# Grease Column number
			"numero":	0,
			"sature":	2
			}
		self.__ingredients = []				# Output list of inported ingredients
		self.__dataFilePath = "./data.pkl"	# Save data fil path
		
	def __importData(self):
		"""Import data from Excel file and remove the old data""" 
		
		for aIdxRow in xrange(self.__sheetNutriments.nrows):
			if aIdxRow > 3 : # Pull title rows
				aTestNum = self.__sheetNutriments.cell(rowx=aIdxRow,colx=self.__valuesColsNutriments["numero"]).value
				try: # Test to avoid other titles
					int(aTestNum)
				except:
					continue
				
				aIngredient = Ingredient()
				
				# Set of each nutriment
				aIngredient.numero = self.__sheetNutriments.cell(rowx=aIdxRow,colx=self.__valuesColsNutriments["numero"]).value
				aIngredient.nom = (self.__sheetNutriments.cell(rowx=aIdxRow,colx=self.__valuesColsNutriments["nom"]).value).encode('utf-8')
				aIngredient.calories = self.__sheetNutriments.cell(rowx=aIdxRow,colx=self.__valuesColsNutriments["calories"]).value
				aIngredient.carbo = self.__sheetNutriments.cell(rowx=aIdxRow,colx=self.__valuesColsNutriments["carbo"]).value
				aIngredient.proteine = self.__sheetNutriments.cell(rowx=aIdxRow,colx=self.__valuesColsNutriments["proteine"]).value
				aIngredient.lipide = self.__sheetNutriments.cell(rowx=aIdxRow,colx=self.__valuesColsNutriments["lipide"]).value
				aIngredient.fibre = self.__sheetNutriments.cell(rowx=aIdxRow,colx=self.__valuesColsNutriments["fibre"]).value
				aIngredient.sodium = self.__sheetNutriments.cell(rowx=aIdxRow,colx=self.__valuesColsNutriments["sodium"]).value
				
				# Append to the imported data list
				self.__ingredients.append(aIngredient)
				
		for aIdxRow in xrange(self.__sheetGrease.nrows):
			if aIdxRow > 3 : # Go to the beginning
				aTestNum = self.__sheetGrease.cell(rowx=aIdxRow,colx=self.__valuesColsGrease["numero"]).value
				try:
					int(aTestNum) # Test to avoid Excel titles
				except:
					continue
				aNumSature = self.__sheetGrease.cell(rowx=aIdxRow,colx=self.__valuesColsGrease["numero"]).value
				self.__ingredients[int(aNumSature)-1].sature = self.__sheetGrease.cell(rowx=aIdxRow,colx=self.__valuesColsGrease["sature"]).value
		
		aDataFile = open(self.__dataFilePath, 'w')
		
		pickle.dump(self.__ingredients, aDataFile)
		
		aDataFile.close()


	def __loadData(self):
		"""Load data from the current database"""		
		aDataFile = open(self.__dataFilePath, 'r')
		self.__ingredients=pickle.load(aDataFile)
		aDataFile.close()
		
	def getIngredients(self):
		"""Retrieve ingredients by different means"""
		if not self.__ingredients: 		# If ingredient list is not setted
			try:
				self.__loadData() 		# Try to load data from database
			except:
				pass
			if not self.__ingredients:	# The database doesn't exist so import from Excel file
				self.__importData()
		return self.__ingredients
	
	def resetData(self):
		"""Import data from Excel file and remove the old data""" 
		self.__importData()
		
	def displayData(self):
		"""Display the database"""
		for aIngredient in self.__ingredients :
			print(str(aIngredient))
			