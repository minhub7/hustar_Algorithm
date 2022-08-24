def create_adjacency_matrix(n, m):
    matrix = [[0]*n for _ in range(n)]
    for _ in range(m):
        u, v, c = map(int, input().split())
        matrix[u][v] = c
    return matrix


def main():
    size = int(input())
    for _ in range(size):
        N, M = map(int, input().split())
        adj_mtrx = create_adjacency_matrix(N, M)
        for mtrx in adj_mtrx:
            print(*mtrx)


if __name__ == '__main__':
    main()
