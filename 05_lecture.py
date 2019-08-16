# N = int(input())
# sum = 0
# for i in range(N, 101):
#     sum += i
# print(sum)

# nums = list(map(int, input().split()))
# cnt3 = 0
# cnt5 = 0
# for i in nums:
#     if i % 3 == 0:
#         cnt3 += 1
#     if i % 5 == 0:
#         cnt5 += 1
# print('Multiples of 3 : {}'.format(cnt3))
# print('Multiples of 5 : {}'.format(cnt5))

# N = int(input())
# scores = list(map(int, input().split()))
# sum = 0
# for i in scores:
#     sum += i
# avg = round(sum/N,1)
# if avg >= 80:
#     print('avg : {} \npass'.format(avg))
# else:
#     print('avg : {} \nfail'.format(avg))  

# for i in range(2,7):
#     print(i, end=' ')
#     for j in range(i+1, i+5):
#         print(j, end=' ')
#     print('')

# for i in range(2, 5):
#     for j in range(1, 6):
#         print('%d * %d = %2d   '%(i, j, i*j), end='')
#     print('')

# N = int(input())
# sum = 0
# cnt = 0
# for i in range(N+1):
#     if i % 2:
#         sum += i
#         cnt += 1
#     if sum >= N:
#         break
# print('{} {}'.format(cnt, sum))

# N = int(input())
# for i in range(1,N+1):
#     a = '*' * i
#     print(a)

# N = int(input())
# for i in range(N,0,-1):
#     a = '*' * i
#     print(a)
# for j in range(1,N+1):
#     b = '*' * j
#     print(b)

# N = int(input())
# for i in range(0, N):
#     a = ' ' * i + '*' * (N-i)
#     print('{}'.format(a))

# N = int(input())
# for i in range(N,0,-1):
#     a = ' '*(N-i) + '*'*(2*i - 1) + ' '*(N-i)
#     print('{}'.format(a))

N = int(input())
# words = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# word = ''
# for j in range(0,N):
#     word += words[j]
# print(word)
# word = ''
# for k in range(N,N+(N-1)):
#     word += words[k]
# print(word)
# word = ''
# for l in range(2*N-1,3*N-3):
#     word += words[l]
# print(word)
# word = ''
alp = ord("A")
for i in range(N,0,-1):
    a = ''
    for j in range(i):
        print(chr(alp), end='')
        alp += 1
    print()
    