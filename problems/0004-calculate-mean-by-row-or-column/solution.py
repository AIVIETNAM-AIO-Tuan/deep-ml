def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	a = len(matrix)
	b = len(matrix[0])
	if mode == 'row':
		for m in matrix:
			total = 0
			for i in m:
				total += i
			mean = total/len(m)
			means.append(mean)
	

	if mode == 'column':
		for i in range(b):
			total = 0
			for j in range(a):
				total = total + matrix[j][i]
			mean = total/a
			means.append(mean)
	return means