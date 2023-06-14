#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Answer1.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detectAndRemovel(head):
    if head is None or head.next is None:
        return

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if slow != fast:
        return

    slow = head

    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    fast.next = None


def ListWithLoop(arr, n, x):
    if n == 0:
        return None

    head = Node(arr[0])
    curr = head
    loopNode = None

    for i in range(1, n):
        newNode = Node(arr[i])
        curr.next = newNode
        curr = curr.next

        if i == x - 1:
            loopNode = curr

    curr.next = loopNode

    return head



# In[ ]:


arr = [1, 3, 4]
n = len(arr)
x = 2

head = ListWithLoop(arr, n, x)

detectAndRemovel(head)

current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")


# In[ ]:


arr = [1,8,3,4]
n = len(arr)
x = 0

head = ListWithLoop(arr, n, x)

detectAndRemovel(head)

current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")


# In[ ]:


arr = [1, 2, 3, 4]
n = len(arr)
x = 1

head = ListWithLoop(arr, n, x)

detectAndRemovel(head)

current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")


# In[ ]:


#Answer 2.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        


def addOne(head):
    if head is None:
        return None

    
    curr = head
    last_non_nine = None
    while curr.next:
        if curr.data < 9:
            last_non_nine = curr
        curr = curr.next

    if curr.data < 9:
        curr.data += 1
    else:
        if last_non_nine is None:
            new_head = Node(1)
            new_head.next = head
            return new_head
        else:
            last_non_nine.data += 1
            curr = last_non_nine.next
            while curr:
                curr.data = 0
                curr = curr.next

    return head



# In[ ]:


def printLinkedList(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

head = Node(4)
node2 = Node(5)
node3 = Node(6)

head.next = node2
node2.next = node3

print("Original Linked List:")
printLinkedList(head)

new_head = addOne(head)

print("Modified Linked List:")
printLinkedList(new_head)


# In[ ]:



head = Node(1)
node2 = Node(2)
node3 = Node(3)

head.next = node2
node2.next = node3

print("Original Linked List:")
printLinkedList(head)

new_head = addOne(head)

print("Modified Linked List:")
printLinkedList(new_head)


# In[ ]:


#Answer 3.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None

def merge(a, b):
    if a is None:
        return b
    if b is None:
        return a
    
    result = None
    if a.data <= b.data:
        result = a
        result.bottom = merge(a.bottom, b)
    else:
        result = b
        result.bottom = merge(a, b.bottom)
    
    result.next = None
    return result

def flatten(root):
    if root is None or root.next is None:
        return root
    
    root.next = flatten(root.next)
    root = merge(root, root.next)
    
    return root

def printList(root):
    while root:
        print(root.data, end="->")
        root = root.bottom


# In[ ]:


head = Node(5)
head.next = Node(10)
head.next.next = Node(19)
head.next.next.next = Node(28)

head.bottom = Node(7)
head.bottom.bottom = Node(8)
head.bottom.bottom.bottom = Node(30)

head.next.bottom = Node(20)

head.next.next.bottom = Node(22)
head.next.next.bottom.bottom = Node(50)

head.next.next.next.bottom = Node(35)
head.next.next.next.bottom.bottom = Node(40)
head.next.next.next.bottom.bottom.bottom = Node(45)

head = flatten(head)

printList(head)


# In[ ]:


head = Node(5)
head.next = Node(10)
head.next.next = Node(19)
head.next.next.next = Node(28)

head.bottom = Node(7)
head.bottom.bottom = Node(8)
head.bottom.bottom.bottom = Node(30)


head.next.next.bottom = Node(22)
head.next.next.bottom.bottom = Node(50)


head = flatten(head)

printList(head)


# In[ ]:


#Answer 4.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def copyRandomList(head):
    if head is None:
        return None
    
    mapping = {}
    curr = head
    while curr:
        new_node = Node(curr.data)
        mapping[curr] = new_node
        curr = curr.next
    
    curr = head
    while curr:
        new_node = mapping[curr]
        new_node.next = mapping.get(curr.next)
        new_node.random = mapping.get(curr.random)
        curr = curr.next
    
    return mapping[head]


# In[ ]:


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

head.random = head
head.next.random = head.next.next.next

copied_head = copyRandomList(head)

curr = copied_head
while curr:
    print("Node:", curr.data)
    if curr.random:
        print("Random Pointer:", curr.random.data)
    else:
        print("Random Pointer: None")
    print("---")
    curr = curr.next


# In[ ]:


head = Node(1)
head.next = Node(3)
head.next.next = Node(5)
head.next.next.next = Node(9)

head.random = head
head.next.random = head.next.next.next

copied_head = copyRandomList(head)

curr = copied_head
while curr:
    print("Node:", curr.data)
    if curr.random:
        print("Random Pointer:", curr.random.data)
    else:
        print("Random Pointer: None")
    print("---")
    curr = curr.next


# In[ ]:


#Answer 5.



class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEven(head):
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    evenHead = even
    evenStart = even

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next

    odd.next = evenStart

    return head


# In[ ]:


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

reorder = oddEven(head)

result = []
node = reorder
while node:
    result.append(node.val)
    node = node.next

print(result)


# In[ ]:


head = Node(2)
head.next = Node(1)
head.next.next = Node(3)
head.next.next.next = Node(5)
head.next.next.next.next = Node(6)
head.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next = Node(7)

reorder = oddEven(head)

result = []
node = reorder
while node:
    result.append(node.val)
    node = node.next

print(result)


# In[ ]:


#Answer 6.

def leftShiftLinked(head, k):
    if not head or k == 0:
        return head

    length = 0
    node = head
    while node:
        length += 1
        node = node.next
    k %= length

    if k == 0:
        return head

    prev = None
    curr = head

    for _ in range(k):
        prev = curr
        curr = curr.next

    prev.next = None

    node = curr
    while node.next:
        node = node.next
    node.next = head

    head = curr

    return head


# In[ ]:


values = [2, 4, 7, 8, 9]
head = Node(values[0])
node = head
for i in range(1, len(values)):
    node.next = Node(values[i])
    node = node.next

k = 3  

shifted = leftShiftLinked(head, k)

result = []
node = shifted
while node:
    result.append(str(node.val))
    node = node.next

print(' '.join(result))


# In[ ]:


values = [1, 2, 3, 4, 5, 6, 7, 8]
head = Node(values[0])
node = head
for i in range(1, len(values)):
    node.next = Node(values[i])
    node = node.next

k = 4 
shifted = leftShiftLinked(head, k)

result = []
node = shifted
while node:
    result.append(str(node.val))
    node = node.next

print(' '.join(result))


# In[ ]:


#Answer 7.

def nextLarger(head):
    values = []
    node = head
    while node:
        values.append(node.val)
        node = node.next

    stack = []
    result = [0] * len(values)

    for i in range(len(values) - 1, -1, -1):
        while stack and values[i] >= values[stack[-1]]:
            stack.pop()

        if stack:
            result[i] = values[stack[-1]]

        stack.append(i)

    return result


# In[ ]:


values = [2, 1, 5]
head = Node(values[0])
node = head
for i in range(1, len(values)):
    node.next = Node(values[i])
    node = node.next

result = nextLarger(head)
print(result)


# In[ ]:


values = [2, 7, 4, 3, 5]
head = Node(values[0])
node = head
for i in range(1, len(values)):
    node.next = Node(values[i])
    node = node.next

result = nextLarger(head)
print(result)


# In[1]:


#Answer 8.



class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSum(head):
    dummy = Node(0)
    dummy.next = head
    cumulative_sum = 0
    node = dummy
    sum_map = {}

    while node:
        cumulative_sum += node.val

        if cumulative_sum in sum_map:
            prev = sum_map[cumulative_sum].next
            curr_sum = cumulative_sum + prev.val
            while prev != node:
                del sum_map[curr_sum]
                prev = prev.next
                curr_sum += prev.val
            sum_map[cumulative_sum].next = node.next
        else:
            sum_map[cumulative_sum] = node

        node = node.next

    return dummy.next


# In[2]:


values = [1, 2, -3, 3, 1]
head = Node(values[0])
node = head
for i in range(1, len(values)):
    node.next = Node(values[i])
    node = node.next

result = removeZeroSum(head)

node = result
while node:
    print(node.val, end=" ")
    node = node.next


# In[6]:


values = [1, 2, 3, -3, 4]
head = Node(values[0])
node = head
for i in range(1, len(values)):
    node.next = Node(values[i])
    node = node.next

result = removeZeroSum(head)

node = result
while node:
    print(node.val, end=" ")
    node = node.next


# In[7]:


values = [1, 2, 3, -3, -2]
head = Node(values[0])
node = head
for i in range(1, len(values)):
    node.next = Node(values[i])
    node = node.next

result = removeZeroSum(head)

node = result
while node:
    print(node.val, end=" ")
    node = node.next


# In[ ]:




