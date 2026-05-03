
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i + 1 
    return -1

lst = [10, 20, 30, 40, 50]
print("List:", lst)
target = int(input("Enter element to search: "))
pos = linear_search(lst, target)
if pos != -1:
    print(f"Element found at position {pos}")
else:
    print("Element not found")
