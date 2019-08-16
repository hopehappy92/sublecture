#1.
'''
n개의 서로 다른 자연수가 주어질 때, 이들 중 최대 값을 찾고
그 값이 몇번째 수인지 구하세요

예를들어, 서로다른 n개의 자연수가 3, 29, 38, 12, 57, 74, 40, 85, 61 이라면
최대값은 85, 그리고 7번째 수

answer = [85, 7]
'''


# #1
# a = input('자연수를 입력하시오: ')

# lst = a.split(',')
# answer = []
# maximum = lst[0]
# count = 0
# for i in lst:
#     if i >= maximum:
#         maximum = i
# answer.append(int(maximum))
# for idx in lst:
#     if idx == maximum:
#         answer.append(count)
#     count += 1

# print(answer)



# #2
# def compare(*args):
#     lst = [*args]
#     answer = []
#     maximum = lst[0]
#     count = 0
#     for i in lst:
#         if i >= maximum:
#             maximum = i
#     answer.append(maximum)
#     for i in lst:
#         if i == maximum:
#             answer.append(count)
#         count += 1
#     return answer
# a = compare(3, 29, 38, 12, 57, 74, 40, 85, 61)
# print(a)



# #3
# lst = [3, 29, 38, 12, 57, 74, 40, 85, 61]
# compare = dict(enumerate(lst))
# max_val = compare.get(0)
# answer = []
# for i in compare.values():
#     if i >= max_val:
#         max_val = i
# answer.append(max_val)
# for i in compare.keys():
#     if compare.get(i) == max_val:
#         answer.append(i)
# print(answer)


#4
lst = [3, 29, 38, 12, 57, 74, 40, 85, 61]
compare = dict(enumerate(lst))
max_val = compare.get(0)
idx_num = 0
answer = []
for i, j in compare.items():
	if j >= max_val:
		max_val = j
		if compare.get(i) == max_val:
			idx_num = i
answer.append(max_val)
answer.append(idx_num)

print(answer)



# # So's
# lst = [3, 29, 38, 12, 57, 74, 40, 85, 61]
# result = []
# max_num = lst[0]
# for i in range(len(lst)):
# 	result = []
# 	if max_num < lst[i]:
# 		max_num = lst[i]
# 	result.append(max_num)
# 	result.append(lst.index(max_num))

# print(result)

# #Ryu' s
# def max_idx(a):
# 	new_lst = []
# 	for i in a:
# 		new_lst.append(i)
# 	a = sorted(new_lst)
# 	b = a[-1]
# 	d = a.index(b)
# 	return [b,d]

# print(max_idx([3, 29, 38, 12, 57, 74, 40, 85, 61]))