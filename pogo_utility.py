#Pokemon Go Utility

import sys
import csv


#Get the command line arguments
#We want the file and desired 

def startPogoUtility():
	for arg in sys.argv:
		if arg = "help":
			helpMenu();
	if len(sys.argv) != 2:
		print "Please give 1 argument when running this script with the name of the utility."

def helpMenu():
	print "Here are the following functions available to you (Argument -> Function): "
	print "ivcalc -> Pogo IV Calculator"
	
def ivCalc():

#Given the name of the pokemon, return its base stats from the file
def getBaseStats(pokemon_name):
	with open('pokemon_base_stats', 'rb') as f:
		file = csv.reader(f)
		for row in file:
			if(row[0].lower == pokemon_name.lower()):
				return row[1:]
	return "not found";

def getIVs():
	ivs = [-1, -1, -1]
	counter = 0
	hasIvs = [False, False, False]
	while !hasIvs[0]:
		ivs[0] = input("Please enter your stamina iv: ")
	while !hasIvs[1]:
		ivs[1] = input("Please enter your attack iv: ")
	while !hasIvs[2]:
		ivs[2] = input("Please enter your defense iv: ")
	
def calculateIvs(base_stats):

#Given the base stats of the pokemon and its ivs, calculate its cp
def calculateCP(ivs, base_stats):
	CP = ((Base Atk + IV)x(Base Def + IV)^0.5 x (Base Stam + IV)^0.5) / 10