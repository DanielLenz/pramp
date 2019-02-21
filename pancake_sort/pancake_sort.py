import numpy as np


def flip(arr, k):
    """
    Reverses the order of the first k elements in arr
        :param arr: 1D array
        :param k: int
    
    Example
    -------
    > arr = [1, 3, 4, 5, 2]
    > k = 3
    > flip(arr, k)
    [4, 3, 1, 5, 2]

    """
    for idx in range(k // 2):
        arr[idx], arr[k - idx - 1] = arr[k-idx - 1], arr[idx]

    return arr

  
def pancake_sort(arr, verbose=0):
    """
    Implements the pancake sorting algorithm.

    For each iteration:
        find n-th largeset element (its index)
        flip(arr, k=idx)
       ` flip(arr, k=len(arr)-n)
    """
    for iteration in range(len(arr)-1):
        max_idx = arr.index(max(arr[:~iteration]))
        arr = flip(arr, k=max_idx+1)
        arr = flip(arr, k=len(arr)-iteration)
        if verbose:
            print(f"Iteration {iteration}: {arr}")

    return arr

def test():
    test_arr = np.random.randint(-100, 100, size=1000).tolist()
    np.testing.assert_array_equal(sorted(test_arr), pancake_sort(test_arr))


if __name__ == '__main__':
    test()
    arr = [1, 5, 6, 8, -1, 4, 3, 2]
    arr = [1, 5]
    print(f"Input array: {arr}")
    sorted_arr = pancake_sort(arr, verbose=1)