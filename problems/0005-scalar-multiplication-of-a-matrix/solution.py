def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result = []
	# matrix = numpy.array(matrix)
	for m in matrix:
		r = []
		for i in m:
			r.append(i*scalar)
		result.append(r)
	return result