def add_lists(a, b):
	"""
		>>> add_lists([1, 1], [1, 1])
		[2, 2]
		>>> add_lists([1, 2], [1, 4])
		[2, 6]
		>>> add_lists([1, 2, 1], [1, 4, 3])
		[2, 6, 4]
	"""
	top = []
	for i in range(len(a)):
		top.append(a[i] + b[i])
	return top

#print add_lists([1, 1], [1, 1])


def mult_lists(a, b):
	"""
		>>> mult_lists([1, 1], [1, 1])
		2
		>>> mult_lists([1, 2], [1, 4])
		9
		>>> mult_lists([1, 2, 1], [1, 4, 3])
		12
	"""
	mult = 0
	for i in range(len(a)):
		mult += (a[i] * b[i])
	return mult

#print mult_lists([1, 2], [1, 4])


def add_row(matrix):
    """
      >>> m = [[0, 0], [0, 0]]
      >>> add_row(m)
      [[0, 0], [0, 0], [0, 0]]
      >>> n = [[3, 2, 5], [1, 4, 7]]
      >>> add_row(n)
      [[3, 2, 5], [1, 4, 7], [0, 0, 0]]
      >>> n
      [[3, 2, 5], [1, 4, 7]]
    """
    a = []
    for i in range(len(matrix[0])):
		a.append(0)
    matrix.append(a)
    return matrix

#print add_row([[3, 2, 5], [1, 4, 7]])


def add_column(matrix):
    """
      >>> m = [[0, 0], [0, 0]]
      >>> add_column(m)
      [[0, 0, 0], [0, 0, 0]]
      >>> n = [[3, 2], [5, 1], [4, 7]]
      >>> add_column(n)
      [[3, 2, 0], [5, 1, 0], [4, 7, 0]]
      >>> n
      [[3, 2], [5, 1], [4, 7]]
    """
    for i in range(len(matrix)):
		matrix[i].append(0)
    return matrix

#print add_column([[3, 2, 5], [1, 4, 7]])


def add_matrices(m1, m2):
    """
      >>> a = [[1, 2], [3, 4]]
      >>> b = [[2, 2], [2, 2]]
      >>> add_matrices(a, b)
      [[3, 4], [5, 6]]
      >>> c = [[8, 2], [3, 4], [5, 7]]
      >>> d = [[3, 2], [9, 2], [10, 12]]
      >>> add_matrices(c, d)
      [[11, 4], [12, 6], [15, 19]]
      >>> c
      [[8, 2], [3, 4], [5, 7]]
      >>> d
      [[3, 2], [9, 2], [10, 12]]
    """
    add = []
    for i in range(len(m1)):
		add.append([])
		for j in range(len(m1[0])):
			add[i].append(m1[i][j] + m2[i][j])
    return add
#a = [[8, 2], [3, 4], [5, 7]]
#b = [[3, 2], [9, 2], [10, 12]]
#print add_matrices(a, b)


def scalar_mult(n, m):
    """
      >>> a = [[1, 2], [3, 4]]
      >>> scalar_mult(3, a)
      [[3, 6], [9, 12]]
      >>> b = [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
      >>> scalar_mult(10, b)
      [[30, 50, 70], [10, 10, 10], [0, 20, 0], [20, 20, 30]]
      >>> b
      [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
    """
    a = []
    for i in range(len(m)):
        a.append([])
        for j in range(len(m[0])):
            a[i].append(n * m[i][j])
    return a

#b = [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
#print scalar_mult(10, b)


def row_times_column(m1, row, m2, column):
    """
      >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 0)
      19
      >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 1)
      22
      >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 0)
      43
      >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 1)
      50
    """


def matrix_mult(a, b):
    """
      >>> matrix_mult([[1, 2], [3,  4]], [[5, 6], [7, 8]])
      [[19, 22], [43, 50]]
      >>> matrix_mult([[1, 2, 3], [4,  5, 6]], [[7, 8], [9, 1], [2, 3]])
      [[31, 19], [85, 55]]
      >>> matrix_mult([[7, 8], [9, 1], [2, 3]], [[1, 2, 3], [4, 5, 6]])
      [[39, 54, 69], [13, 23, 33], [14, 19, 24]]
    """
    #~ c = []
    #~ for i in range(len(a)):
        #~ c.append([])
        #~ for j in range(len(m[0])):
            #~ c[i]
    #~ return c
#~ if __name__ == '__main__':
	#~ import doctest
	#~ doctest.testmod()