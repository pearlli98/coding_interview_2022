# you can write to stdout for debugging purposes, e.g.
print("This is a debug message")

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

# specification 
# param: head (head node of a linked list)
#        k (non-negative integer)
# return value of kth to last element of a singly linked list
# if k > length of list, return -1
# if k <= 0, return -1
# if linked list contains cycle, return -1

def checkForCycle(head):
    if not head:
        return False
    slow = head
    fast = head.next
    while slow and fast:
        if slow == fast:
            return True
        if not fast.next or not fast.next.next:
            break
        else:
            slow = slow.next
            fast = fast.next.next
    return False

def getKthToLast(head, k):

    if k <= 0 or checkForCycle(head):
        return -1

    total_count = 0
    pointer = head
    while pointer != None:
        total_count += 1
        pointer = pointer.next
    
    if total_count < k:
        return -1

    current_count = 0
    result = head
    while current_count != total_count - k:
        current_count += 1
        result = result.next
    
    return result.value

# test:
# parititon on linked list length: =0, 1, >1
# partition on k: k = 0, 0 < k < N, k = N, k > N
# partition on output: -1, >= 0

# test 1
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
k1 = 2
print('test1')
print(getKthToLast(head1, k1))
print('------------------------')

# test 2
# empty list
print('test2')
print(getKthToLast(None, 1))
print('------------------------')

# test 3
# one node valid output
head3 = Node(1)
print('test3')
print(getKthToLast(head3, 1))
print('------------------------')

# test 4
# one node k out of bound
head4 = Node(1)
print('test4')
print(getKthToLast(head4, 2))
print('------------------------')

# test 5
# one node k = 0
head5 = Node(1)
print('test5')
print(getKthToLast(head5, 0))
print('------------------------')

# test 6
# longer list
head6 = Node(1)
head6.next = Node(2)
head6.next.next = Node(3)
head6.next.next.next = Node(4)
head6.next.next.next.next = Node(5)
head6.next.next.next.next.next = Node(6)
print('test6')
print(getKthToLast(head6, 4))
print(getKthToLast(head6, 6))
print(getKthToLast(head6, 7))
print('------------------------')

# test 7
# negative k
head7 = Node(1)
print('test7')
print(getKthToLast(head7, -1))
print('------------------------')

# test 8
# circular list
head8 = Node(1)
head8.next = Node(2)
head8.next.next = Node(3)
head8.next.next.next = head8
print('test8')
print(getKthToLast(head8, 2))
print('------------------------')

# test 9
# circular list
head8 = Node(1)
head8.next = Node(2)
head8.next.next = Node(3)
head8.next.next.next = head8.next
print('test9')
print(getKthToLast(head8, 2))
print('------------------------')



