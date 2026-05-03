
def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

lst = [64, 25, 12, 22, 11]
print("Original List:", lst)
sorted_lst = selection_sort(lst)
print("Sorted List:", sorted_lst)
