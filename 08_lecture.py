import sys
sys.stdin = open('08_lecture_snail.txt')

def safe(y, x):
    return (0 <= y < N) and (0 <= x < N) and data[y][x] == 0

def snail(data):
    y, x = 0, 0
    newy, newx = 0, 0
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    direction = 0
    num = 1
    for i in range(N*N):
        y, x = newy, newx
        data[y][x] = num
        newy = y + dy[direction]
        newx = x + dx[direction]
        if not safe(newy, newx):
            direction = (direction + 1) % 4
            newy = y + dy[direction]
            newx = x + dx[direction]
        num += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [[0 for _ in range(N)] for _ in range(N)]

    snail(data)

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(data[i][j], end=' ')
        print()



# def solve(lst):
#     global N
#     X, Y = 0, 0
#     newX, newY = 0, 0
#     dy = [0, 1, 0, -1]
#     dx = [1, 0, -1, 0]
#     dir_stat = 0 # 0: 오른, 1: 아래, 2: 왼, 3:위
#     num = 1
#     for i in range(N*N):
#         X, Y = newX, newY
#         lst[Y][X] = num
#         newX = X + dx[dir_stat]
#         newY = Y + dy[dir_stat]
#         if newY >= N or newX >= N or newY < 0 or newX < 0 or lst[newY][newX] != 0:
#             dir_stat = (dir_stat + 1) % 4
#             newX = X + dx[dir_stat]
#             newY = Y + dy[dir_stat]
#         num += 1

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     data = [[0 for _ in range(N)] for _ in range(N)]

#     solve(data)

#     print('#{}'.format(tc))
#     for i in range(N):
#         for j in range(N):
#             print(data[i][j], end=' ')
#         print()