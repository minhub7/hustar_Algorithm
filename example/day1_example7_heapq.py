import heapq

def main():
    size = int(input())
    for _ in range(size):
        hq = []
        query = int(input())
        for q in range(query):
            n = int(input())
            print(heapq.heappop(hq)) if n == -1 else heapq.heappush(hq, n)


if __name__ == '__main__':
    main()
