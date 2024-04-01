def selection_sort(lst):
    for i in range(len(lst)-1):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        if i != min_index:
            lst[min_index],lst[i] = lst[i], lst[min_index]
    return lst
           

lst = [4,2,6,5,1,3]

print(selection_sort(lst))




# lst = [4,2,6,5,1,3]
# min_index = 0
# st = 1
# for st in range(1, len(lst)):
#     for i in range(st,len(lst)):
#         if lst[i] < lst[min_index]:
#             min_index = i
#     print('before: ',lst)
#     lst[st-1], lst[min_index] = lst[min_index], lst[st-1]
#     min_index = st
#     print(lst)



# print(lst)
    



