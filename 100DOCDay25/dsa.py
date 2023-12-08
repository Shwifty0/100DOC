# TODO
# Binary Search

lst = [1, 6, 12, 10, 9, 7]
target = 10
def binary_search(lst, target):
    sorted_list = sorted(lst)
    l, r = 0, len(sorted_list) - 1
    
    while l <= r:
        m = (l + r) // 2
        if sorted_list[m] > target:
            r = m - 1
        if sorted_list[m] < target:
            l = m + 1
    return -1

# TODO
# Bubble Sort
def bubble_sort(lst):
    sort_list = []
    for i in range(len(lst)-1):
        for j in range((len(lst) - 1) - i):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
                sort_list = lst
    return sort_list

# TODO
# Palindrome
str = 'racecar'

def palindrome(str):
    return str[-1::-1]

#print(palindrome(str))

# TODO
# Check if the sequence is in the list

lst1 = [1,2,3,4,5]
lst2 = [2,3]

def check(lst1, lst2):
    index = []
    for num in lst2:
        if num in lst1:
            index.append(lst1.index(num))
    return index

#print(check(lst1, lst2))

# TODO
# Swapping 
a = 20
b = 30

a = a + b
b = a - b
a = a - b

#print(a, b)

ls1 = [1,2,3,4,5,6]
ls2 = [1,2,3,4,5,6]

sum = 0
for i in range(len(ls1)-1):
    cur_sum = ls1[i] + ls2[i]
    sum += cur_sum
    print(sum)