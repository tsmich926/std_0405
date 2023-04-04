di=[1,1,-1,-1,1]
dj=[-1,1,1,-1,1]
def dfs(n, ci, cj, v):
    global ans, si, sj
    if n>3:
        return
    if n==3 and (ci,cj)==(si,sj) and ans<len(v):
        ans = len(v)

    for dr in range(n, n+2):
        ni,nj = ci+di[dr], cj+dj[dr]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] not in v:
            dfs(dr, ni, nj, v + [arr[ni][nj]])

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for si in range(N):
        for sj in range(N):
            dfs(0, si, sj, [])

    print(f'#{test_case} {ans}')