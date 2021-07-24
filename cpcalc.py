import csv
import itertools as it

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
	CP = calculateCPHelper(levelScaler, ivs, base_stats)
	return CP

#formula to calculate the CP
def calculateCPHelper(levelScaler, ivs, base_stats):
	CP = ((ivs[1] + base_stats[1])*(ivs[2] + base_stats[2])**0.5 * (ivs[0] + base_stats[0])**0.5) * levelScaler/ 10.0;
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
		
def cpCalcConfig(args):
	ivs = getIVs()
	base_stats = getBaseStats(args[1])
	print calculateCP(ivs, base_stats)

def getRaidCPs(name):
	base_stats = getBaseStats(name)
	#don't need level; just specific calls for level constant
	normal = getLevelConstant(20)
	weather = getLevelConstant(25)

	#go through calculations twice, once with normal and once with weather boost
	#consider all IP combinations (between 10s and 15s)
	possible_vals = {'A': [10, 11, 12, 13, 14, 15], 'D': [10, 11, 12, 13, 14, 15], 'S': [10, 11, 12, 13, 14, 15]}
	all_options = sorted(possible_vals)

	generated_combinations = it.product(*(possible_vals[comb] for comb in all_options))
	unique_combinations = list(generated_combinations)

	#normal combinations print
	for c in unique_combinations:
		print str(c) + ": " + str(calculateCPHelper(normal, c, base_stats))
	#weather boosted combinations print
	for c in unique_combinations:
		print str(c) + ": " + str(calculateCPHelper(weather, c, base_stats))
