class Company:
    def __init__(self, name, average):
        self.name = name
        self.avarage = average

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, company):
    if root is None:
        return Node(company)
    if company.avarage > root.data.avarage: 
        root.right = insert(root.right, company)
    else: 
        root.left = insert(root.left, company)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data.name, root.data.avarage)
        inorder(root.right)


def delete_incorrect_company(root, low, high):
    if root is None:
        return None
    if root:
        root.left = delete_incorrect_company(root.left, low, high)
        root.right = delete_incorrect_company(root.right, low, high)
        if root.data.avarage < low:
            root = root.right
        elif root.data.avarage > high:
            root = root.left
    return root
N = int(input())
low, high = list(map(int ,input().split()))

root = None

for i in range(N):
    companyName = input()
    costList = list(map(int, input().split()))
    avarage = sum(costList) / len(costList)
    company = Company(companyName, avarage)
    root = insert(root, company)

inorder(root)
print()
root = delete_incorrect_company(root, low, high)
inorder(root)