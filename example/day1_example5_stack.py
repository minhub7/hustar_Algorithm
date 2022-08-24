def main():
    size = int(input())
    for _ in range(size):
        stack = []
        query = int(input())
        for q in range(query):
            n = int(input())
            print(stack.pop()) if n == -1 else stack.append(n)

if __name__ == '__main__':
    main()
