# mls by danamic programming
def maxSubarray(arr):
    if len(arr) == 1:
        return arr[0]
    cache = [arr[0]]
    for i in range(1, len(arr)):
        cache.append(max(0, cache[-1]) + arr[i])
    return max(cache)


def main():
    size = int(input())
    for _ in range(size):
        arr = list(map(int, input().split()))
        print(maxSubarray(arr))


if __name__ == '__main__':
    main()
