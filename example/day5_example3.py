def world_memorization(n, m):
    score_board = [list(map(int, input().split())) for _ in range(n)]
    mp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                mp[i][j] = score_board[i][j]
            elif i == 0 and j > 0:
                mp[i][j] = mp[i][j-1] + score_board[i][j]
            elif i > 0 and j == 0:
                mp[i][j] = mp[i-1][j] + score_board[i][j]
            else:
                mp[i][j] = min([mp[i-1][j], mp[i][j-1], mp[i-1][j-1]]) + score_board[i][j]

    return mp[-1][-1]


def main():
    size = int(input())
    for _ in range(size):
        n, m = map(int, input().split())
        print(world_memorization(n, m))

'''
2
3 4
4 0 0 0
0 2 3 4
1 3 5 2
3 5
1 1 2 1 1
1 2 1 2 1
1 1 1 1 1

'''

if __name__ == '__main__':
    main()
