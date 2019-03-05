def isToeplitz(arr):

    if (not arr) or (len(arr) == 1) or (len(arr[0]) == 1):
        return True

    n_row = len(arr)
    n_col = len(arr[0])

    for i in range(n_row-1):
        if arr[i][:n_col-1] != arr[i+1][1:]:
            return False

    return True


if __name__ == "__main__":
    matrix = [
            [1,2,3,4],
            [5,1,2,3],
            [6,5,1,2]]


    print(isToeplitz(matrix))