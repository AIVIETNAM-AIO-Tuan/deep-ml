import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	result = np.zeros(len(scores), dtype = float)
	total = sum(np.exp(i - max(scores)) for i in scores)

	for i in range(len(scores)):
		result[i]  = scores[i] - max(scores) - np.log(total)
	return result
