def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # # Your code here
    # n = len(a)
    # # a = numpy.array(a)
    # i = 1
    # b = []
    # while i < n:
    #     r = list(zip(a[i-1],a[i]))
        
    #     b.append(r)
       
    #     print(i)
    #     i = i +1
    a = list(zip(*a))
    a = [list(i) for i in a]
    return a
    # a = numpy.array(a)
    # a = a.T

    # return a.tolist()