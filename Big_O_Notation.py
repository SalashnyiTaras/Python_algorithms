""" O-Complexity or Big-O analysis or asymptotic analysis
    We use it to define which algorithm is better.
    How we do it - the idea bases on interdependence between runtime and input size"""
"""Big O Examples"""

# # Time complexity = runtime
# # Constant O(1)
# def func_constant(values):
#     print(values[0])
#
#
# # no matter how big input, function will take only first value
# func_constant([1, 2, 3])


# # Linear O(n)
# def func_linear(lis):
#     for i in lis:
#         print(i)
#
#
# # as much bigger input becomes, as much bigger output becomes
# func_linear([1, 2, 3, 4, 5, 6, 7])


# # Tricky Linear1 O(n)
# def func_linear1(lis1):
#     for i in lis1:
#         print(i)
#     for i in lis1:
#         print(i)
# # as much bigger input becomes, the complexity of this function is 2(n), 2 - is a constant, when we reach big
# values, constants do not matter any more ==> the complexity becomes O(n)
# func_linear1([1, 2, 3, 4, 5, 6, 7])


# # Tricky Linear2 O(n)
# def func_linear2(lis2):
#     print(lis2[0])
#
#     midpoint = len(lis2)//2
#
#     # interesting that we can slice list and use the result as iterable in for loop
#     for i in lis2[:midpoint]:
#         print(i)
#
#     for i in range(10):
#         print('name')
#
#
# # here we have got some mathematiacal operations like // and constants, but in bigger scale, they will not matter. Important is
# # still the complexity is the same - O(n)
# func_linear2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# # Quadratic O(n^2)
# def func_linear(lis):
#     counter = 0
#     for i in lis:
#         for j in lis:
#             print(i, j)
#             counter += 1
#     print(counter)
#
#
# # the output is n^2 of inputs. For instance, nested loops, if we use have list [1,2,3], the output will be 9
# func_linear([1, 2, 3, 4, 5, 6])

# # Space complexity
# # we check how much memory an algorithm uses
# def memory(n):
#     for x in range(n):  # time complexity is O(n)
#         print('Memory!')  # space complexity is O(1)
#
#
# memory(10)














