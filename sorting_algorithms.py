from random import randint
from timer_decorator import timer


# @timer
# def bubble_sort(nums):
#     """bubble sorting realization"""
#     for i in range(len(nums) - 1):
#         for j in range(len(nums) - i - 1):
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#
# random_list_of_nums = [randint(0, 10) for i in range(100)]
# bubble_sort(random_list_of_nums)
# print(random_list_of_nums)
#


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    # if len(arr) == 1:
    #     return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


arr = [3, 4, 7, 9, 1, 6]
n = len(arr)
quick_sort(arr, 0, n - 1)


