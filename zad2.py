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

def find_closest_number(root, target):
    closest = root.data
    while root is not None:
        if abs(root.data - target) < abs(closest - target):
            closest = root.data
        if target < root.data:
            root = root.left
        else:
            root = root.right
    return closest

value = int(input())
number = int(input())
firstNum = int(input())
root = Node(firstNum)
for i in range(number - 1):
    insert(root, int(input()))
    
print(find_closest_number(root, value))

    
