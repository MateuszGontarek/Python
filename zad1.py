class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, new_data):
    if root is None:
        return Node(new_data)
    if new_data > root.data: 
        root.right = insert(root.right, new_data)
    else: 
        root.left = insert(root.left, new_data)
    return root

def func(root, target):
    if root:
        func(root.left, target)
        dict[root.data] = target - root.data
        func(root.right, target)
    
target = int(input())
numbers = list(map(int, input().split()))
root = Node(numbers[0])
dict = {}
for i in range(1, len(numbers)):
    insert(root, numbers[i])

func(root, target)
    
for i in dict:
    if i + dict[i] == target:
        print(numbers.index(i), numbers.index(dict[i]))
        break
        