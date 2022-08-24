from collections import deque

def main():
    size = int(input())
    for _ in range(size):
        n = int(input())
        ranking = deque()
        change = 'NO'
        rank = list(map(int, input().split()))
        for r in rank:
            if r in ranking and ranking.count(r) == n - 1:
                c = ranking.popleft()
                if r != c:
                    change = "YES"
                    break
            else:
                ranking.append(r)
        print(change)

if __name__ == '__main__':
    main()