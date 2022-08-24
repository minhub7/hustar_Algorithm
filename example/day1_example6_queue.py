from collections import deque

def main():
    size = int(input())
    for _ in range(size):
        queue = deque()
        query = int(input())
        for q in range(query):
            n = int(input())
            print(queue.popleft()) if n == -1 else queue.append(n)


if __name__ == '__main__':
    main()
