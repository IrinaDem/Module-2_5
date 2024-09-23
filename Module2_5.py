def get_matrix(n, m, value):
        matrix = list()
        for i in range(n):
            row = [value] * m
            matrix.append(row)
        return matrix
matrix = get_matrix(2, 2, 10)
for row in matrix:
    print(row)

