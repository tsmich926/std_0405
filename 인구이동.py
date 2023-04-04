from collections import deque


n, l, r = map(int, input().split())
popularity = [list(map(int, input().split())) for _ in range(n)]
day = 0
graph = dict()

def check(value, input, x, y): # 인구 이동 조건 확인
    if (input >= l) and (input <= r):
        value.append((x, y))

def border(i, j): 
    value = []
    if i-1 >= 0:
        top = abs(popularity[i-1][j]-popularity[i][j])      
        check(value, top, i-1, j)
    if i+1 < n:
        bottom = abs(popularity[i+1][j]-popularity[i][j])
        check(value, bottom, i+1, j)
    if j-1 >= 0:
        left = abs(popularity[i][j-1]-popularity[i][j])
        check(value, left, i, j-1)
    if j+1 < n:
        right = abs(popularity[i][j+1]-popularity[i][j])
        check(value, right, i, j+1)
    if value:
        graph[(i, j)] = value