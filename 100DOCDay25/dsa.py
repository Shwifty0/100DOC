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

print(bubble_sort(lst))