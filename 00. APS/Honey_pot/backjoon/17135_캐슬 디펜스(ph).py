def kill(k, y):
    xx, yy, min_d = - 1, - 1, 100
    for i in range(k - 1, -1, -1):
        for j in range(M):
            if mat[i][j] and not killed[i][j]:
                td = abs(i - k) + abs(j - y)
                if td < min_d:
                    xx, yy, min_d = i, j, td
                elif td == min_d and j < yy:
                    xx, yy = i, j

    return (min_d <= D, xx, yy)


def solve(k):
    if k == 0:
        return
    else:
        t = []
        t.append(kill(k, archer[0]))
        t.append(kill(k, archer[1]))
        t.append(kill(k, archer[2]))
        for found, x, y in t:
            if found:
                killed[x][y] = 1
        solve(k - 1)


N, M, D = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

archer = [0] * 3
ans = 0
for i in range(M - 2):
    for j in range(i + 1, M - 1):
        for k in range(j + 1, M):
            killed = [[0] * M for _ in range(N)]
            archer[0], archer[1], archer[2] = i, j, k
            solve(N)
            ans = max(ans, sum(sum(killed, [])))
print(ans)