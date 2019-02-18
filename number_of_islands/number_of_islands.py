from collections import deque
from copy import deepcopy
import numpy as np


def get_number_of_islands(matrix, method='dfs'):
    matrix = deepcopy(matrix)
    width, height = len(matrix[0]), len(matrix)

    count = 0
    for row in range(height):
        for col in range(width):
            if matrix[row][col] == 1:
                if method == 'dfs':
                    dfs(matrix, row, col)
                else:
                    bfs(matrix, row, col)
                count += 1

    return count


def is_valid(matrix, row, col):
    width, height = len(matrix[0]), len(matrix)

    in_box = (
            row >= 0 and
            col >= 0 and
            col < width and
            row < height)

    if not in_box:
        return False
    else:
        return matrix[row][col] == 1


def dfs(matrix, row, col):
    # Check if we're stepping outside the box
    # or if the entry is not 1
    if not is_valid(matrix, row, col):
        return

    # Set visited to 0
    matrix[row][col] = -1

    dfs(matrix, row-1, col)
    dfs(matrix, row+1, col)
    dfs(matrix, row, col+1)
    dfs(matrix, row, col-1)


def bfs(matrix, row, col):

    queue = deque()
    queue.appendleft((row, col))

    while queue:
        r, c = queue.pop()
        matrix[r][c] = -1

        if is_valid(matrix, r-1, c):
            queue.appendleft((r-1, c))
        if is_valid(matrix, r+1, c):
            queue.appendleft((r+1, c))
        if is_valid(matrix, r, c-1):
            queue.appendleft((r, c-1))
        if is_valid(matrix, r, c+1):
            queue.appendleft((r, c+1))
    return


if __name__ == '__main__':
    test_matrix = [
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 1],
    ]
    # print(get_number_of_islands(test_matrix, method='bfs'))
    assert get_number_of_islands(test_matrix, method='dfs') == 3
    assert get_number_of_islands(test_matrix, method='bfs') == 3