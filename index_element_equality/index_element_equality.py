    # Sorted arr
    # Distinct

def index_equals_value_search(arr):
    # Edge cases
    if not arr:
        return -1
    if len(arr) == 1:
        return 0 if arr[0] == 0 else -1
    if (arr[0] > 0) or (arr[-1] < len(arr) - 1):
        return -1

    # Normal case, use two pointers
    lowest_so_far = -1
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        middle = (lo+hi) // 2
        # If equal, return
        if middle == arr[middle]:
            lowest_so_far = middle
            hi = middle - 1
        # If value is smaller than index, set lo = middle + 1
        if arr[middle] < middle:
            lo = middle + 1
        # If value is larger than index, set hi = middle - 1
        if arr[middle] > middle:
            hi = middle - 1

    return lowest_so_far


if __name__ == '__main__':
    arr = [-8,0,2,5]
    arr = [-1,0,3,6]
    arr = [-1, 1, 2, 3, 4, 5, 6, 7]
    print(index_equals_value_search(arr))
