import numpy as np

def spiral_copy(matrix):
    width, height = len(matrix[0]), len(matrix)
    if not (width and height):
        return []

    if height == 1:
        return matrix[0]

    if width == 1:
        return [row[0] for row in matrix]

    flat = []


    #  row = 0, height
    #  col = 0, width

    n_shell = 0
    while min(width, height) / 2. > n_shell:
        row = n_shell

        # Top row
        for col in range(n_shell, width - n_shell):
            flat.append(matrix[row][col])

        # Right column
        col = width - n_shell - 1
        for row in range(n_shell+1, height - n_shell - 1):
            flat.append(matrix[row][col])

        # Bottom row
        row = height - n_shell - 1
        for col in range(width - n_shell -1, n_shell, -1):
            flat.append(matrix[row][col])

        # Left column
        col = n_shell
        for row in range(height - n_shell - 1, n_shell, -1):
            flat.append(matrix[row][col])

        n_shell += 1

    return flat

if __name__ == '__main__':
    test_matrix  = [
    [1,    2,   3,  4,    5],
    [6,    7,   8,  9,   10],
    [11,  12,  13,  14,  15],
    [16,  17,  18,  19,  20]]

    #  test_matrix = np.arange(25).reshape((5,5))

    print(np.array(test_matrix))

    print(spiral_copy(test_matrix))
  
  
  
  
  
  
  
  
  