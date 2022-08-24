# 가중치가 없는 무방향 그래프 - 인접 리스트
def create_graph(N, M):  # N = 노드 수, M = 간선 수
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    return graph


def dfs_stack(arr, u):
    stack = arr[u]
    visited = [False] * len(arr)  # len(arr) = 4, case 1
    visited[u] = True
    sequence = [u]
    while stack:
        v = stack.pop()
        if not visited[v]:
            sequence.append(v)
            visited[v] = True
            stack.extend(sorted(arr[v], reverse=True))
    return sequence


def ransonware(N, M, K):
    ranson_graph = create_graph(N, M)
    seq = dfs_stack(ranson_graph, K)
    return N - len(seq)


def main():
    size = int(input())
    for _ in range(size):
        N, M, K = map(int, input().split())
        print(ransonware(N, M, K))


if __name__ == '__main__':
    main()
