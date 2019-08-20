# N = int(input())
# alp = ord("A")
# cnt = 1
# for i in range(N,0,-1):
#     for j in range(i):
#         print(cnt, end=' ')
#         cnt += 1
#     for k in range(N-i+1):
#         print(chr(alp), end=' ')
#         alp += 1
#     print()
    
# lst = ''.join(list(input().split()))
# print(lst)

# lst = [2, 1, 4, 3, 5, 9, 8, 7, 6, 10]
# for i in range(len(lst)):
#     for j in range(len(lst)):
#         if lst[i] <= lst[j]:
#             lst[i], lst[j] = lst[j], lst[i]
# print(' '.join(map(str, lst)))

# lst = ''.join(list(input().split()))
# print('{} {} {}'.format(lst[0], lst[3], lst[6]))

# lst = []
# while True:
#     a = str(input())
#     if a == '0':
#         break
#     lst.append(a)
# print(' '.join(lst[-2::-1]))

# lst = list(map(str, input().split()))
# print(' '.join(lst[-2::-1]))

# lst = [85.6, 79.5, 83.1, 80.0, 78.2, 75.0]
# n = list(map(int, input().split()))
# avg = round((lst[n[0]-1] + lst[n[1]-1]), 1)
# print(avg)

# lst = list(map(int, input().split()))
# min = 987654321
# for i in lst:
#     if i < min:
#         min = i
# print(min)

# lst = list(map(int, input().split()))
# min = 987654321
# max = 0
# for i in lst:
#     if i < 100:
#         if i > max:
#             max = i
#     if i >= 100:
#         if i < min:
#             min = i
# if max == 0:
#     max = 100
# if min == 987654321:
#     min = 100
# print('{} {}'.format(max, min))

# lst = list(map(int, input().split()))
# even = 0
# odd = 0
# for i in range(0,len(lst),2):
#     odd += lst[i]
# for j in range(1, len(lst),2):
#     even += lst[j]
# oddavg = round(odd/5, 1)
# print('sum : {} \navg : {}'.format(even, oddavg))

# lst = list(map(int, input().split()))
# for i in range(len(lst)):
#     for j in range(len(lst)):
#         if lst[i] > lst[j]:
#             lst[i], lst[j] = lst[j], lst[i]
# print(' '.join(map(str, lst)))

lst = list(map(str, input().split()))
dic = {}
llst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M' ,'N', 'O', 'P', 'Q', 'R' ,'S', 'T','U', 'V', 'W', 'X', 'Y','Z']
for i in lst[:-1]:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
for i in llst:
    for val in dic.values():
        print('{} : {}'.format(i, val))