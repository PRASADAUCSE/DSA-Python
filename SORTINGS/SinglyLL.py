class Node:
    """Node class for singly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(10)
n2 = Node(20)
n3 = Node(40)


n1.next = n2
n2.next = n3


def insert_first(head, data):
    print(head)
    temp = Node(data)
    temp.next = head
    return temp

def insert_last(head, data):
    temp = Node(data)
    dummy_head = head
    while(dummy_head.next != None):
        dummy_head = dummy_head.next
    dummy_head.next = temp
    return head

def printLL(head):
    dummy_head = head
    while(dummy_head != None):
        print(dummy_head.data)
        dummy_head = dummy_head.next

def get_length(head):
    size =0
    dummy_head = head
    while(dummy_head != None):
        size+=1
        dummy_head = dummy_head.next
    return size

head = insert_last(n1, 76)
head = insert_first(head, 24)
#printLL(head)

length = get_length(head)
def insert_at(head, data, pos):
    if(pos == 0 or pos == 1):
        return insert_first(head, data)
    ct=1
    dummy_head = head
    temp = Node(data)
    while(ct < pos-1):
        dummy_head = dummy_head.next
        ct+=1
    temp.next = dummy_head.next
    dummy_head.next = temp
    return head


updated_ll = insert_at(head, 99, 2)
printLL(updated_ll)