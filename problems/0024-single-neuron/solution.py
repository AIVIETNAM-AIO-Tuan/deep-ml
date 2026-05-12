import math
# import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	n = len(features)
	f = [sum(i*y for i,y in zip(x,weights))+ bias for x in features] 

	# for i in f:
	probabilities = [1/(1+math.exp(-i)) for i in f] 
	mse = 0
	for i in range(len(f)):
		mse += (probabilities[i] - labels[i])**2
	mse = mse*1/n
	return probabilities, mse