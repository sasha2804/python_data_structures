
l1 = [2,4,3]
l2 = [5,6,4]


mult = 1
num1 = 0

for i in range(len(l1)-1, -1, -1):

    num1 += l1[i]*mult
    mult *= 10



print(num1)