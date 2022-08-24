def power(n, k, m):
    if k == 0:
        return 1
    if k == 1:
        return n
    half = power(n, k//2, m)

    return (half * half) % m if k % 2 == 0 else (half * half * n) % m


def main():
    size = int(input())
    for _ in range(size):
        n, k, m = map(int, input().split())
        print(power(n, k, m))


if __name__ == '__main__':
    main()
