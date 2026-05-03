import math

def indexed_search(lst, target):
    block_size = int(math.sqrt(len(lst)))
    start = 0
    while start < len(lst) and lst[min(start + block_size - 1, len(lst)-1)] < target:
        start += block_size
    for i in range(start, min(start + block_size, len(lst))):
        if lst[i] == target:
            return True
    return False

lst = [5, 10, 15, 20, 25, 30]
print("List:", lst)
target = int(input("Enter element: "))
if indexed_search(lst, target):
    print("Element found")
else:
    print("Element not found")
