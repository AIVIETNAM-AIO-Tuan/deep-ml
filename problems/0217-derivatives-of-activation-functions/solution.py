import numpy as np
def sigmoid(x: float) -> float:
	return 1/(1+np.power(np.e, x))
def tanh(x: float) -> float:
	return (np.power(np.e, x)-np.power(np.e, -x))/(np.power(np.e, x)+np.power(np.e, -x))
def ReLU(x: float) -> float:
	return max(0,x)
def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	grad_sig = sigmoid(x)*(1-sigmoid(x))
	grad_tanh = 1 - np.power(tanh(x), 2)
	grad_relu = 1 if (x>0) else 0

	return {'sigmoid':float(grad_sig), 'tanh':float(grad_tanh), 'relu':grad_relu}