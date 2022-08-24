"""
    마을회관 건설
"""

def main():
    size = int(input())
    for _ in range(size):
        town = list(map(int, input().split()))
        cost = [abs(t - town[len(town) // 2]) for t in town]
        print(sum(cost))

if __name__ == '__main__':
    main()