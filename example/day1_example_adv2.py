from itertools import combinations

def slope(p, q):
    return abs((p[1]-q[1])/(p[0]-q[0]))


# def main():
#     size = int(input())
#     for _ in range(size):
#         num_coord = int(input())
#         coordinates = [tuple(map(int, input().split())) for _ in range(num_coord)]
#         comb_coord = list(combinations(coordinates, 2))
#         S = [(idx, grad(p, q)) for idx, (p, q) in enumerate(comb_coord)]
#         max_idx = max(S, key=lambda x: x[1])
#         answer = sorted(comb_coord[max_idx[0]])
#         print(f"coordinates: {coordinates}")
#         print(f"comb_coord: {comb_coord}")
#         print(f"S: {S}")
#         print(f"max_idx: {max_idx}")
#         print(f"comb_coord[max_idx]: {comb_coord[max_idx[0]]}")
#         print(*answer[0], *answer[1])

def main():
    size = int(input())
    for _ in range(size):
        num_coord = int(input())
        coordinates = [tuple(map(int, input().split())) for _ in range(num_coord)]
        print(f"coordinates: {coordinates}")
        min_value = []

        for idx, (cx, _) in enumerate(coordinates[:-1]):
            diff_x = [(idx2, abs(cx - x)) for idx2, (x, _) in enumerate(coordinates[idx+1:], start=idx+1)]
            min_value.append([idx, min(diff_x, key=lambda x: x[1])])

        min_ = []
        for m in min_value:
            if m[1][1] == min(min_value, key=lambda x: x[1][1])[1][1]:
                min_.append(m)
        min_x = [(coordinates[m[0]], coordinates[m[1][0]]) for m in min_]
        print(f"min_x: {min_x}")

        max_value = []

        for idx, (_, cy) in enumerate(coordinates[:-1]):
            diff_y = [(idx2, abs(cy - y)) for idx2, (_, y) in enumerate(coordinates[idx + 1:], start=idx + 1)]
            max_value.append([idx, min(diff_y, key=lambda x: x[1])])

        max_ = []
        for m in max_value:
            if m[1][1] == max(max_value, key=lambda x: x[1][1])[1][1]:
                max_.append(m)
        max_y = [(coordinates[m[0]], coordinates[m[1][0]]) for m in max_]
        print(f"max_y: {max_y}")


if __name__ == '__main__':
    main()
