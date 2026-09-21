import numpy as np
def derivative(x:list[float], i:int) -> list[float]:
	s = []
	for j in range(len(x)):
		if j == i:
			s.append(x[j]*(1-x[j]))
		else:
			s.append(-x[j]*x[i])
	return s
def softmax_derivative(x: list[float]) -> list[list[float]]:
	"""
	Compute the Jacobian matrix of the softmax function.
	
	Args:
		x: Input vector of real numbers
		
	Returns:
		Jacobian matrix J where J[i][j] = d(softmax_i)/d(x_j)
	"""
	sum_exp = sum(np.power(np.e, k) for k in x)
	s = [np.power(np.e, k)/sum_exp for k in x]
	output = []
	for i in range(len(s)):
		output.append(derivative(s,i))
	return output