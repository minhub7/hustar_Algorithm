from collections import deque

def merge(arr1, arr2):
    arr1 = deque(arr1)
    arr2 = deque(arr2)
    merged = []
    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] <= arr2[0]:
            merged.append(1)
            arr1.popleft()
        else:
            merged.append(2)
            arr2.popleft()

    for _ in range(len(arr1)):
        merged.append(1)
    for _ in range(len(arr2)):
        merged.append(2)

    return merged

# def merge_sort(arr):
#     half = len(arr) // 2
#     if len(arr) <= 1:
#         return arr
#     elif len(arr) == 2:
#         sol = arr
#         if arr[0] > arr[1]:
#             sol = [arr[1], arr[0]]
#         return sol
#     else:
#         left = merge_sort(arr[:half])
#         right = merge_sort(arr[half:])
#         return merge(left, right)


def main():
    size = int(input())
    for _ in range(size):
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        print(*merge(arr1, arr2))


if __name__ == '__main__':
    main()
