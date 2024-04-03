

def insertion_sort(lst):
    for i in range(1, len(lst)):
        while i != 0 and lst[i-1] > lst[i]:
            lst[i-1], lst[i] = lst[i], lst[i-1]
            i -= 1
    return lst            
    

lst = [4,2,6,5,1,3]


print(insertion_sort(lst))