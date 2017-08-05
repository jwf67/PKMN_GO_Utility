#Pokemon Go Utility

import sys
import csv
import evolxpcalc
import cpcalc


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
	print "evolxpcalc <pokemon name> (ex. evolxpcalc pidgey) -> Pogo Evolution XP Calculator (id: 2)"
	if restart == 1:
		print "Restart to use properly. Bye."
	
def navigateOptions(args):
	if args[0] == "cpcalc":
		cpcalc.cpCalcConfig(args)
	elif args[0] == "evolxpcalc":
		evolxpcalc.getInput(args[1])
	else:
		print "Not found."
	doMore()
	
#asks the user whether he/she wants to do anything else
def doMore():
	response = raw_input("Would you like to do anything else? (yes, anything else for no): ")
	if response == "yes":
		helpMenu(0)
		function = raw_input("Enter your preferred function: ")
		species = raw_input("Enter your desired pokemon: ")
		args = [function, species]
		navigateOptions(args)
	


#Run the functions
startPogoUtility()