# better solution
def bubble_sort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):        
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


# # worse solution
# def bubble_sort(lst):
#     while True:
#         count = 0
#         for i in range(0, len(lst)-1):        
#             if lst[i] > lst[i+1]:
#                 lst[i], lst[i+1] = lst[i+1], lst[i]
#             else:
#                 count += 1
#         if count == len(lst) - 1:
#             break
#     return lst


# lst1 = [2,4,6,5,1,3]


# print(bubble_sort(lst1))


