def calculate_tax(tax):
    coin = {50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0}
    for c in coin.keys():
        if tax // c:
            coin[c] += tax // c
            tax %= c
    return coin


def main():
    size = int(input())
    for _ in range(size):
        tax = int(input())
        print(sum(calculate_tax(tax).values()))


if __name__ == '__main__':
    main()