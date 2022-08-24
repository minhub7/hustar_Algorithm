size = int(input())
for _ in range(size):
    idx_list = list(map(int, input().split()))
    print(max(idx_list) - min(idx_list))