lst = [2,4,5,6,9,12,20,50]
target = 4

def binary_search(lst, target):
    
    l, r = 0, len(lst) - 1
    
    while l <= r:
        m = (l + r) // 2
        number = lst[m]
        if number > target:
            r = m - 1
        elif number < target:
            l = m + 1
        else:
            return m

print(binary_search(lst, target))