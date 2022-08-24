import math

def heavyweight_liquid(N, C):
    liquid = [tuple(map(int, input().split())) for _ in range(N)]
    liquid.sort(key=lambda s: s[0]/s[1], reverse=True)
    weight = 0
    for liq in liquid:
        if C > liq[1]:
            weight += liq[0]
            C -= liq[1]
        else:
            weight += C * (liq[0] / liq[1])
            break
    return math.floor(weight)


def main():
    size = int(input())
    for _ in range(size):
        n, c = map(int, input().split())
        print(heavyweight_liquid(n, c))


if __name__ == '__main__':
    main()