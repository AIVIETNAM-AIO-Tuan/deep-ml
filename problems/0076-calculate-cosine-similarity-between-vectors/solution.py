import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	if (len(v1)==0 or len(v2) == 0 or len(v1) != len(v2)):
		return None;
	v1 = np.array(v1)
	v2 = np.array(v2)
	dot = v1 @ v2
	mag = np.sqrt(np.sum(v1**2)) * np.sqrt(np.sum(v2**2))
	# mag = np.linalg.norm(v1) + np.linalg.norm(v2)
	
	return dot / mag
	pass