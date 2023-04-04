
N, M = map(int, input().split())

r, c, d = map(int, input().split())

r_d = [-1, 0, 1, 0]
c_d = [0, 1, 0, -1]
# 방향설정 북 동 남 서
room = [list(map(int, input().split())) for _ in range(N)]
clean = [[False] * M for _ in range(N)]
now_r = r
now_c = c

ans = 0
clean[now_r][now_c] = True
ans += 1

while True:
    change = 0
    while change < 4:
        rotate = (d - 1) % 4  # 회전방향
        r_r = now_r + r_d[rotate]
        r_c = now_c + c_d[rotate]
        if room[r_r][r_c] == 0 and clean[r_r][r_c] == False:
            d = rotate
            now_r = r_r
            now_c = r_c
            clean[now_r][now_c] = True
            ans += 1
            break
        else:
            d = rotate
            change += 1

    if change == 4:
        back_p = (d - 2) % 4  # 뒤로 가는 방향 만들어줌
        back_r = now_r + r_d[back_p]
        back_c = now_c + c_d[back_p]
        if room[back_r][back_c] == 0:
            now_r = back_r
            now_c = back_c
        else:
            break

print(ans)