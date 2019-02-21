"""
Is a sub-problem of the edit distance, which turns out to best a very minor modification.
We use the iterative approach, which overcomes the memory issues we'd run into with the
recursive approach.
"""


def deletion_distance(str1, str2):
    if not (str1 or str2):
        return 0

    m, n = len(str1) + 1, len(str2) + 1

    if not str1:
        return len(str2)

    if not str2:
        return len(str1)

    """
        a b c
    0 1 2 3
    b 1 1 1 2
    c 2 2 2 1
    d 3 3 3 2
    """

    table = [[0 for _ in range(n)] for _ in range(m)]

    # Initiate column 0
    for i in range(m):
        table[i][0] = i

    # Initiate row 0
    for j in range(n):
        table[0][j] = j

    # Iterate through table
    for i in range(1, m):
        for j in range(1, n):
            if str1[i-1] == str2[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = 1 + min(
                    table[i-1][j],
                    table[i][j-1])
            
    return table[-1][-1]


if __name__ == '__main__':
    t1, t2 = 'dog', 'frog'

    print(deletion_distance(t1, t2))

