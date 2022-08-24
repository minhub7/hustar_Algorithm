from bisect import bisect_left

def binary_search(arr, target):
    if target >= arr[-1]:
        return arr[-1]
    idx = bisect_left(arr, target)
    if abs(target - arr[idx-1]) <= abs(target - arr[idx]):
        return arr[idx-1]
    else:
        return arr[idx]


def main():
    size = int(input())
    for _ in range(size):
        arr = list(map(int, input().split()))
        target = list(map(int, input().split()))
        answer = [binary_search(arr, t) for t in target]
        print(*answer)


if __name__ == '__main__':
    main()
