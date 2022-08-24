def knapsack(n, C):
    W = list(map(int, input().split()))
    V = list(map(int, input().split()))
    D = [[0] * (C + 1) for _ in range(n)]

    for i in range(n):
        for j in range(1, C+1):
            if i == 0:
                if W[i] > j:
                    D[i][j] = 0
                else:
                    D[i][j] = V[i]
            else:
                if W[i] > j:
                    D[i][j] = D[i-1][j]
                else:
                    D[i][j] = max(D[i-1][j], D[i-1][j-W[i]] + V[i])

    return D[n-1][C]


def main():
    size = int(input())
    for _ in range(size):
        n, C = map(int, input().split())
        print(knapsack(n, C))


if __name__ == '__main__':
    main()
