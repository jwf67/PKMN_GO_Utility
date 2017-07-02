#Pokemon Go Utility

import sys
import csv
import evolxpcalc


#Get the command line arguments
#We want the file and desired 

def startPogoUtility():
	args = sys.argv
	for arg in args:
		if arg == "help":
			helpMenu(1)
			quit()
	if len(args) != 3:
		print "Please give 2 argument when running this script with the name of the utility."
	else:
		navigateOptions(args[1:])

def helpMenu(restart):
	print "Here are the following functions available to you (Argument -> Function): "
	print "cpcalc <pokemon name> (ex. cpcalc vaporeon) -> Pogo CP Calculator (id: 1)"
	print "evolxpcalc <pokemon name> (ex. ecolxpcalc pidgey) -> Pogo Evolution XP Calculator (id: 2)"
	if restart == 1:
		print "Restart to use properly. Bye."
	
def navigateOptions(args):
	if args[0] == "cpcalc":
		cpCalcConfig(args)
	elif args[0] == "evolxpcalc":
		evolxpcalc.getInput(species)
	else:
		print "Not found. Bye."
	
#asks the user whether he/she wants to do anything else
def doMore():
	response = input("Would you like to do anything else? (1 for yes, anthing else for no): ")
	if response == 1:
		helpMenu(0)
		function = input("Enter your preferred function's id:")
		species = input("Enter your desired pokemon: ")
		

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
				row[1:] = [float(i) for i in row[1:]]
				print row
				return row[1:]
				#for python3, return list(map(int ,row[1:])
	return "not found";

def getLevel():
	level = 0
	validLevel = False
	while not validLevel:
		level = input("Please enter your pokemon's level: ")
		if (isinstance(level, int) or isinstance(level, float)):
			validLevel = isValidLV(level)
	return float(level)
	
def isValidLV(level):
	if 1 <= level and level <= 40:
		return True
	return False
	
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
	ivs = [float(i) for i in ivs]
	print ivs
	return ivs

def validIV(iv):
	if iv >= 0 and iv <= 15:
		return True
	return False
	
def calculateIvs(base_stats):
	return null

#Given the base stats of the pokemon and its ivs, calculate its cp
def calculateCP(ivs, base_stats):
	level = getLevel()
	levelScaler = getLevelConstant(level)
	CP = ((ivs[1] + base_stats[1])*(ivs[2] + base_stats[2])**0.5 * (ivs[0] + base_stats[0])**0.5) * levelScaler/ 10.0
	return CP
	
#https://gaming.stackexchange.com/questions/280491/formula-to-calculate-pokemon-go-cp-and-hp
def getLevelConstant(level):
	if 1 <= level and level <= 10:
		return ( 0.01885225 * level ) - 0.01001625
	if 10.5 <= level and level <= 20:
		return ( 0.01783805 * ( level - 10 ) ) + 0.17850625
	if 20.5 <= level and level <= 30:
		return ( 0.01784981 * ( level - 20 ) ) + 0.35688675
	if 30.5 <= level and level <= 40:
		return ( 0.00891892 * ( level - 30 ) ) + 0.53538485

#Run the functions
startPogoUtility()