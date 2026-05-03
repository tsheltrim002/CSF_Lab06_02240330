
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def to_list(self):
        return self.items.copy()

def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

stack = Stack()
for val in [34, 12, 5, 67, 23]:
    stack.push(val)

lst = stack.to_list()
print("Stack as list:", lst)
print("Sorted list:", selection_sort(lst))
