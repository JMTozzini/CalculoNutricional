#! /usr/bin/python

from model import Model
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

gModel = Model()
gOption = sys.argv[1]

if (gOption == '1') :
	for aIngredient in gModel.getIngredients():
		print(aIngredient)
else :
	print('Erreur d\'option')