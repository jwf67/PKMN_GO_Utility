#Pokemon Go Utility

import sys
import csv


#Get the command line arguments
#We want the file and desired 

def startPogoUtility():
	args = sys.argv
	for arg in args:
		if arg == "help":
			helpMenu()
			quit()
	if len(args) != 3:
		print "Please give 2 argument when running this script with the name of the utility."
	else:
		navigateOptions(args[1:])

def helpMenu():
	print "Here are the following functions available to you (Argument -> Function): "
	print "cpcalc <pokemon name> (ex. cpcalc vaporeon) -> Pogo CP Calculator"
	print "Restart to use properly. Bye."
	
def navigateOptions(args):
	if args[0] == "cpcalc":
		cpCalcConfig(args)
	else:
		print "Not found. Bye."

def cpCalcConfig(args):
	ivs = getIVs()
	base_stats = getBaseStats(args[1])
	print calculateCP(ivs, base_stats)
	

def ivCalc():
	return null

#Given the name of the pokemon, return its base stats from the file
def getBaseStats(pokemon_name):
	with open('pokemon_base_stats.csv', 'rb') as f:
		file = csv.reader(f)
		for row in file:
			#print row[0].lower()
			if(row[0].lower() == pokemon_name.lower()):
				row[1:] = [int(i) for i in row[1:]]
				print row
				row[1:] = convertIntsToFloats(row[1:])
				return row[1:]
				#for python3, return list(map(int ,row[1:])
	return "not found";

def getIVs():
	ivs = [-1, -1, -1]
	counter = 0
	hasIvs = [False, False, False]
	while not hasIvs[0]:
		ivs[0] = input("Please enter your stamina iv: ")
		if isinstance(ivs[0], int) and validIV(ivs[0]):
			hasIvs[0] = True
	while not hasIvs[1]:
		ivs[1] = input("Please enter your attack iv: ")
		if isinstance(ivs[1], int) and validIV(ivs[1]):
			hasIvs[1] = True
	while not hasIvs[2]:
		ivs[2] = input("Please enter your defense iv: ")
		if isinstance(ivs[2], int) and validIV(ivs[2]):
			hasIvs[2] = True
	ivs = convertIntsToFloats(ivs)
	return ivs

def validIV(iv):
	if iv >= 0 and iv <= 15:
		return True
	return False
	
def calculateIvs(base_stats):
	return null

#Given the base stats of the pokemon and its ivs, calculate its cp
def calculateCP(ivs, base_stats):
	CP = ((ivs[1] + base_stats[1])*(ivs[2] + base_stats[2])^0.5 * (ivs[0] + base_stats[0])^0.5)/ 10
	return CP
	
def convertIntsToFloats(arr):
	for a in arr:
		float(a)
	return arr

#Run the functions
startPogoUtility()