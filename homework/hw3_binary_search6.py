from bisect import bisect_right


def binary_search(arr, target):
    if target >= arr[-1]:
        return 0
    idx = bisect_right(arr, target)
    return len(arr) - idx


def main():
    size = int(input())
    for _ in range(size):
        arr = sorted(list(map(int, input().split())))
        target = list(map(int, input().split()))
        answer = [binary_search(arr, t) for t in target]
        print(*answer)


if __name__ == '__main__':
    main()
