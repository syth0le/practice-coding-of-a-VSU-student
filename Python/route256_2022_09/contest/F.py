class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


t = int(input())
n = int(input())

start = None
if n >= 1:
    value, left, right = list(map(int, input().split()))
    start = Tree(value)
    leftTree = Tree(left)
    rightTree = Tree(right)
    start.left = leftTree
    start.right = rightTree

    value, left, right = list(map(int, input().split()))
    if value == start.left:
        start.left.left = Tree(left)
    if value == start.right:
        start.right.right = Tree(right)

    print(start.left.left)
# for i in range(n-1):
#     value, left, right = list(map(int, input().split()))
#     if value == start.left:
#         start.left.left = Tree(left)
#     if value == start.right:
#         start.right.right = Tree(right)

