
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def is_empty(self):
        return len(self.items) == 0
    def to_list(self):
        return self.items.copy()

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i + 1
    return -1

queue = Queue()
for val in [10, 20, 30, 40, 50]:
    queue.enqueue(val)

lst = queue.to_list()
print("Queue as list:", lst)
target = int(input("Enter element to search: "))
pos = linear_search(lst, target)
if pos != -1:
    print(f"Element found at position {pos}")
else:
    print("Element not found")
