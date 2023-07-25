import random

def generateMatrix(seed=None):
    """
    Genera una matriz de 5x5 con enteros aleatorios entre 0 y 9

    >>> test_matrix = generateMatrix(2)
    >>> print(test_matrix)
    [[0, 1, 1, 5, 2], [4, 4, 9, 3, 9], [0, 9, 2, 6, 6], [8, 5, 8, 7, 8], [4, 0, 0, 5, 7]]

    """
    if seed is not None:
        random.seed(seed)
    matrix = []
    for _ in range(5):
        row = [random.randint(0,9) for _ in range(5)]
        matrix.append(row)
    return matrix

def findConsecutiveSequence(matrix):
    """

    Encuentra 4 números consecutivos en horizontal o vertical

    >>> horizontal_test_matrix = generateMatrix(8)
    >>> print(horizontal_test_matrix)
    [[3, 5, 6, 2, 3], [0, 1, 2, 3, 8], [3, 6, 0, 7, 7], [7, 6, 7, 9, 3], [6, 1, 7, 3, 0]]
    >>> print(findConsecutiveSequence(horizontal_test_matrix))
    ((1, 0), (1, 3))

    >>> vertical_test_matrix = generateMatrix(58)
    >>> print(vertical_test_matrix)
    [[9, 3, 3, 3, 0], [3, 7, 6, 5, 4], [4, 7, 9, 6, 4], [9, 1, 0, 7, 3], [7, 1, 7, 8, 6]]
    >>> print(findConsecutiveSequence(vertical_test_matrix))
    ((1, 3), (4, 3))

    """
    # horizontal sequence
    for row in matrix:
        for i in range(2):
            if row[i]+1 == row[i+1] and row[i]+2 == row[i+2] and row[i]+3 == row[i+3]:
                return ((matrix.index(row),i), (matrix.index(row), i + 3))

    # vertical sequence
    for j in range(5):
        for i in range(2):
            if matrix[i][j] + 1 == matrix[i + 1][j] and matrix[i][j] + 2 == matrix[i + 2][j] and matrix[i][j] + 3 == matrix[i + 3][j]:
                return ((i, j), (i + 3, j))
    return None



if __name__ == "__main__":
    import doctest
    doctest.testmod()
