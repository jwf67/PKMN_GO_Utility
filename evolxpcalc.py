import math

#calculate how many evolutions can be completed and how much experience pokemon go
EVOL_XP = 500
LUCKY_EGG_MULTIPLIER = 2

#take in number of evolutions capable and whether a lucky egg is being used, return amount of xp
class EvolutionsIteration(object):

	
	def __init__(self, id, name, num_pokemon, num_candies, num_candiesforevo):
		self.id = id
		self.name = name
		self.num_pokemon = num_pokemon
		self.num_candies = num_candies
		self.num_candiesforevo = num_candiesforevo
		self.num_evolutions = self.calcEvos()
		
	def calcEvos(self):
		#values to store the number of pokemon and candies remaining before evolution
		remaining_num_pokemon = self.num_pokemon
		remaining_num_candies = self.num_candies
		
		#how many evolutions have been computed so far
		temp_num_evolutions = 0
		
		#Reward for evolving
		reward = 1
		
		print self.num_candiesforevo / remaining_num_pokemon
		print remaining_num_candies / self.num_candiesforevo
		
		#While pokemon still can evolve and candies exist
		while remaining_num_pokemon > 0 and remaining_num_candies > 0 and reward > 0:
			temp_unboundPossibleEvos = self.unboundPossibleEvos()
			temp_evolutionsCandiesPokemon = self.evolutionsCandiesPokemon()
			
			if remaining_num_pokemon <= remaining_num_candies/self.num_candiesforevo:
				reward = pokemon
			else:
				reward = remaining_num_candies/self.num_candiesforevo
				
			temp_num_evolutions = temp_num_evolutions + reward
			
			remaining_num_pokemon = self.num_pokemon - temp_num_evolutions
			remaining_num_candies = self.num_candies - (temp_num_evolutions * self.num_candiesforevo) + temp_num_evolutions
		
		print "final result: %d" % (temp_num_evolutions)
		print "remaining pokemon: %d" % (remaining_num_pokemon)
		print "remaining candies: %d" % (remaining_num_candies)
		self.num_evolutions = temp_num_evolutions
		
		
		
				
					
	def evolutionsCandiesPokemon(self):
		return math.floor(self.num_candiesforevo/self.num_pokemon)
		
	def unboundPossibleEvos(self):
		return math.floor(self.num_candies/self.num_candiesforevo)

	def transferAmt(self):
		unboundPossible = self.unboundPossibleEvos()
		
		if self.num_pokemon <= unboundPossible:
			return self.num_pokemon
		else:
			return self.num_pokemon - unboundPossible
			
	def calcXP(self, lEgg):
		totalXP = self.num_evolutions*EVOL_XP
		
		if lEgg:
			return totalXP
		else:
			return totalXP*LUCKY_EGG_MULTIPLIER
			
	def printProperties(self):
		print self.id, self.name, self.num_pokemon, self.num_candies, self.num_candiesforevo, self.num_evolutions
			
def getInput(species):
	EvolutionIterationList = []
	
	addAnother = True
	
	id = 0
	
	while addAnother:
		EvolutionIterationList.append(getEntryDetails(id))
		
		print "Added the entry. Your current list is the following: "
		printAllEvolutionIterations(EvolutionIterationList)
		
		id = id + 1
		
		response = raw_input("Would you like to add or change an entry (y for yes, c for change, anything else for no)")
		
		if response == "c":
			id_to_change = input("What item would you like to change (enter the id): ")
			EvolutionIterationList[id_to_change] = getEntryDetails(id_to_change, species)	
		elif response != "y":
			addAnother = False
			print "Thanks for utilizing this tool."
			
def getEntryDetails(id, species):
	num_pokemon = input("How many of this pokemon do you have?: ")
	num_candies = input("How many candies do you have for this species?: ")
	num_candiesforevo = input("How many candies does it take to evolve this pokemon?: ")
	
	return EvolutionsIteration(id, species, num_pokemon, num_candies, num_candiesforevo)

def printAllEvolutionIterations(list):
	print "ID | NAME | COUNT | CANDIES | REQUIRED"
	for index in range(0, len(list)):
			print list[index].printProperties()
	
def initiateTests():
	for index in range(30, 100):
		curr_obj = EvolutionsIteration(index - 30, "pidgey", index, 300, 12)
		print "%d pidgeys yielded evolutions" % (index)

	
		







		
	