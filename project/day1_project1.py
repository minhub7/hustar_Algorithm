def check_brk(brk):
    stack = []
    for b in brk:
        if b in ['[', '(', '{']:
            stack.append(b)
        else:
            if not stack:
                return 0
            c = stack.pop()
            if (c != '[' and b == ']') or (c != '(' and b == ')') or (c != '{' and b == '}'):
                return 0

    return len(stack) == 0


def main():
    size = int(input())
    for _ in range(size):
        brk = input()
        print('YES') if check_brk(brk) else print('NO')


if __name__ == '__main__':
    main()