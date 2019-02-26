import numpy as np

def array_of_array_products(arr):
    """Viterbi algorithm, forward-backward algorithm
    """

    # Edgecase
    length = len(arr)
    if length <= 1:
        return []

    # Alloc output N * [1]
    output = [1] * length

    # We use a forward and a backward pass through the array

    # Forward
    p = 1
    for idx in range(length):
        output[idx] *= p
        p *= arr[idx]

    # Backward
    p = 1
    for idx in range(length):
        output[~idx] *= p
        p *= arr[~idx]

    return output


if __name__ == '__main__':
    test_arr = [2, 7, 3, 4]
    output = array_of_array_products(test_arr)

    np.testing.assert_array_equal(
        np.array([84, 24, 56, 42]),
        np.array(output)
    ) 
    print(f"Input: {test_arr}\nOutput: {output}")

    # Edgecases
    # arr = [1]
    # arr = []

    # Out: [84, 24, 56, 42]
    # Forward pass:
    #   p = arr[0]
    #   p= 2, [1, 2, 1, 1]
    #   p= 14, [1, 2, 14, 1]
    #   p= 42, [1, 2, 14, 42]

    # Backward pass
    # p = arr[-1]
    # p= 4, [1, 2, 56, 42]
    # p= 12, [1, 24, 56, 42]
    # p= 84, [84, 24, 56, 42]
  