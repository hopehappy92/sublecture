import sys
sys.stdin = open('09_lecture.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cube = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(4)]

    for i in range(N):
        cube[0][i] = list(map(int, input().split()))
    
    for z in range(3):
        for y in range(N):
            for x in range(N):
                cube[z+1][x][N-1-y] = cube[z][y][x]
                
    print('#{}'.format(tc))
    for y in range(N):
        for z in range(1,4):
            for x in range(N):
                print(cube[z][y][x], end='')
            print(' ', end='')
        print()


# 100 - 101- 102 - 200 - 201- 202 - 300- 301- 302
# 110 - 111- 112 - 210 - 211 - 212


# 000 - 102
# 001 - 112
# 002 - 122

# 010 - 101
# 011 - 111
# 012 - 121

# 020 - 100
# 021 - 110
# 022 - 120
