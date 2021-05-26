from timer_decorator import timer

# num = []
# numbers = [num.append(i) for i in range(1, 10000000)]
#
#
# @timer
# def num_sum(x):
#     """finding sum of all elements: O(n)"""
#     var_sum = 0
#     for i in x:
#         var_sum += i
#     return var_sum
#
#
# @timer
# def num_sum_speeded_up(x):
#     """finding sum of all elements: O(1)"""
#     last_num = x[-1]
#     var_sum = (last_num * (last_num + 1))/2
#     return var_sum
#
#
# print(f"Sum when O(n): {num_sum(num)}")
# print(f"Sum when O(1): {num_sum_speeded_up(num)}")

# checking for duplicates
duplicates = set()
numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    if numbers.count(i) > 1:
        duplicates.add(i)
if len(duplicates) != 0:
    print('Duplicates are:', end=' ')
    for i in duplicates:
        print(i, end=' ',)
else:
    print('No duplicates in a array')