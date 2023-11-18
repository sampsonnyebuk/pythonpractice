

def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
     square = [x*x for x in row]
     result.append(square)
    return result



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
