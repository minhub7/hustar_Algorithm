size = int(input())
for _ in range(size):
    a, b = map(int, input().split())
    print(sum((a, b)))