def tripleGO(n):
    bridge = [0] + list(map(int, input().split()))
    if n == 1:
        return bridge[n]
    elif n == 2:
        return max(bridge[1] + bridge[2], bridge[2])

    dp = [0] * (n+1)
    dp[1] = bridge[1]
    dp[2] = max(bridge[1] + bridge[2], bridge[2])
    for i in range(3, n+1):
        if i % 3 == 0:
            dp[i] = max(dp[i-1], dp[i-2], dp[i//3]) + bridge[i]
        else:
            dp[i] = max(dp[i-1], dp[i-2]) + bridge[i]

    return dp[-1]


def main():
    size = int(input())
    for _ in range(size):
        n = int(input())
        print(tripleGO(n))


if __name__ == '__main__':
    main()