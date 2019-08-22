# import sys
# sys.stdin = open('07_lecture_midavg.txt')

# # def sort(data):
# #     max = 0
# #     for i in range(len(data)):
# #         if data[max] < data[i]:
# #             data[i], data[max] = data[max], data[i]
# #             max = i
            

# T = int(input())
# for tc in range(1, T+1):
#     data = list(map(int, input().split()))
#     ans = 0
#     max = 0
#     min = 987654321
#     sum = 0

#     for i in data:
#         if max < i:
#             max = i
#     data.remove(max)
#     for i in data:
#         if min > i:
#             min = i
#     data.remove(min)
#     for i in data:
#         sum += i
#     ans = round(sum/len(data))

#     print('#{} {}'.format(tc, ans))



# import sys
# sys.stdin = open('07_lecture_fly.txt')

# T = int(input())

# def sumsquare(i, j, M):
#     total = 0
#     for y in range(M):
#         for z in range(M):
#             total += datas[i+y][j+z]
#     return total

# def fly_killer(N, M):
#     max = 0
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             total = sumsquare(i, j, M)
#     if total > max:
#         max = total
#     return max

# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     datas = []
#     for i in range(N):
#         data = list(map(int, input().split()))
#         datas.append(data)

#     result = fly_killer(N, M)
#     print('#{} {}'.format(tc, result))

# T = int(input())
# for tc in range(1, T+1):
#     N, M = list(map(int, input().split()))
#     data = [[0 for _ in range(N)] for _ in range(N)]
#     for i in range(N):
#         data[i] = list(map(int, input().split()))

#     max = 0
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             ans = 0
#             for k in range(M):
#                 for l in range(M):
#                     ans += data[i+k][j+l]
#             if max < ans:
#                 max = ans

#     print('#{} {}'.format(tc, max))



import sys
sys.stdin = open('07_lecture_farm.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input()))
    ans = 0

    m = N//2
    s = m
    e = m + 1
    for i in range(N):
        for j in range(s,e):
            ans += data[i][j]
        if i < m:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print('#{} {}'.format(tc, ans))