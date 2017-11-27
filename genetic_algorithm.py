#Genetic Algorithm
from random import random
from random import randint
from operator import add

#the GA function itself
def evolve(phenotypeArray,diversityRange,mutationScale,populationNumber,retain_value, random_select, mutate_value):
	phenotypeSorted = sorted(phenotypeArray,key=lambda x: x[1])	#population sorted in ascending order
	retain_len = int(len(phenotypeSorted)*retain_value)
	parents = phenotypeSorted[:retain_len]

	for i in range(len(parents)):
		parents[i] = parents[i][0]

	#randomly adding other individuals to promote diversity
	for individual in range(diversityRange):
	    if random_select > random():
	        parents.append([random(),random(),random(),random()])

	#mutate some individuals based on the mutate_value
	for individual in parents:
	    if mutate_value > random():
	        mutation_position = randint(0, len(individual)-1)
	        individual[mutation_position] = max(0,min(1,individual[mutation_position]*(1+mutationScale*(1-random()*2))))

	#crossover parents to create children
	parents_len = len(parents)
	desired_len = populationNumber - parents_len
	children = []
	while len(children) < desired_len:
	    male = randint(0, parents_len-1)
	    female = randint(0, parents_len-1)
	    if male != female:
	        male = parents[male]
	        female = parents[female]
	        half = len(male) / 2
	        #the child takes half of its dad's and half of its mom's genes (can play around with this value)
	        child = male[:half] + female[half:]
	        children.append(child)
	parents.extend(children)

	print parents

	return parents
