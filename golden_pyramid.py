TRIANGLE  = [[7],
            [2, 3],
            [3, 3, 1],
            [3, 1, 5, 4],
            [3, 1, 3, 1, 3],
            [2, 2, 2, 2, 2, 2],
            [5, 6, 4, 5, 6, 4, 3]]


def golden_pyramid(triangle):
    tr = [a[:] for a in triangle]
    for i in range(len(tr)-2, -1, -1):
        for j in range(i+1):
            tr[i][j] += max(tr[i+1][j], tr[i+1][j+1])
            print(i, j, tr[i][j])
    return tr[0][0]


if __name__ == "__main__":
    print(golden_pyramid(TRIANGLE))
