#question 1: debugging for making descending tree

# This program reorders binary trees to be descending. The tree is descending 
# if all children of a node are less than or equal to the node. For example, 
# the following tree is descending:
#        7
#      /  \
#     4    3
#
# The following is not:
#        3
#      /  \
#     5    8
#
# This tree can be made descending by swapping 8 and 3.
#
# Right now, this program is broken. Your job is to make it work. Start with 
# the test cases at the bottom, which create various trees, reorder them and
# verify them to be descending. Some of these are failing. Note that the test 
# function and is_descending function work correctly, so no need to 
# focus on those for debugging, though it may help to read them to 
# understand what they do.

# Encapsulates the data for a single node in a binary tree, including
# its value and its children.
class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def reorder(node):
    if node is None: return

    left = node.left
    right = node.right
    
    reorder(left)
    reorder(right)
        
    # If left and right are both <=, we're good
    if ((left is None or left.value <= node.value) and 
        (right is None or right.value <= node.value)):
        return

    # Find the larger child to swap with if one of the children is >
    swap = left
    if (left is None or (right is not None and left.value < right.value)):
        swap = right

    # Swap values with child
    tmp = swap.value
    swap.value = node.value
    node.value = tmp

    # Now reorder children
    reorder(left)
    reorder(right)
    
#************************************
# There are no bugs below this point.
#************************************

def is_descending(node):
    if node is None:
        return True

    if ((node.left is None or node.left.value <= node.value) and
        (node.right is None or node.right.value <= node.value)):
        
        return is_descending(node.left) and is_descending(node.right)

    return False

def test(node):
    if is_descending(node):
        print('Test Passed')
    else:
        print('Test Failed')

#     5
#   /  \
#  4    1
root = Node(5)
root.left = Node(4)
root.right = Node(1)
reorder(root)
test(root)

#     1
#   /  \
#  4    5
root = Node(1)
root.left = Node(4)
root.right = Node(5)
reorder(root)
test(root)
print(root.value)
print(root.left.value)
print(root.right.value)


#     3
#   /  \
#  8    2
root = Node(3)
root.left = Node(8)
root.right = Node(2)
reorder(root)
test(root)
print(root.value)
print(root.left.value)
print(root.right.value)
        
#       6
#     /  \
#    4    5
#  /  \
# 7    2
root = Node(6)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(7)
root.left.right =  Node(2)
reorder(root)
test(root)
print(root.value)
print(root.left.value)
print(root.right.value)
print(root.left.left.value)
print(root.left.right.value)

#               5
#             /   \
#           9      1
#         /  \    / \
#       2     4  5   4
#     /  \  /  \
#    3   7 1   1
root = Node(5)
root.left = Node(9)
root.right = Node(1)
root.left.left = Node(2)
root.left.right =  Node(4)
root.right.left = Node(5)
root.right.right =  Node(4)
root.left.left.left = Node(3)
root.left.left.right =  Node(7)
root.left.right.left = Node(1)
root.left.right.right =  Node(1)
reorder(root)
test(root)

# question 2: rearrange a string so that no adjacent letters are the same, return -1 if not possible
