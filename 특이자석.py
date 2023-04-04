def dfs():



T = int(input())
for tc in range(1,1+T):
    k = int(input())
    wheel = [list(map(int,input().split())) for _ in range(4)]
    arr = [list(map(int,input().split())) for _ in range(k)]

    for q in arr:
        check = [0 for _ in range(4)]

        dfs(q[0]-1,q[1])



    print('#{} {}'.format(tc,res))
