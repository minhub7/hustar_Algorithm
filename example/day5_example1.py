def cross_bridge(n):
    T = [1, 2, 4]
    if n < 4:
        return T[n-1]

    for i in range(3, n):
        T.append((T[i-3] + T[i-2] + T[i-1]))

    print(T)
    return T[-1]

'''
6
1
2
3
4
5
10

'''
def main():
    size = int(input())
    for _ in range(size):
        n = int(input())
        print(cross_bridge(n))


if __name__ == '__main__':
    main()