class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

n1 = Node(10)
n2 = Node(20)
n3 = Node(40)
n1.prev = None
n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
def printLL(head):
    dummy_head = head
    while(dummy_head != None):
        print(dummy_head.data)
        dummy_head = dummy_head.next

#length function
def length(head):
    size = 0
    while(head != None):
        size+=1
        head = head.next
    return size



#Insertions

#at beginning
def insert_first(head, data):
    temp = Node(data)
    temp.next = head
    head.prev = temp
    return temp


#at tail
def insert_last(head, data):
    temp = Node(data)
    dummy_head = head
    while(dummy_head.next != None):
        dummy_head = dummy_head.next
    dummy_head.next = temp
    temp.prev = dummy_head
    return head


n1 = insert_first(n1, 5)
updated_ll = insert_last(n1, 50)
updated_ll = insert_last(updated_ll, 60)


#at middle
def insert_middle(head, val):
    temp = Node(val)
    middle = length(head)//2
    dummy_head = head
    ct=0
    while(ct< middle-1):
        ct+=1
        dummy_head = dummy_head.next
    
    temp.next = dummy_head.next
    dummy_head.next = temp
    # temp.prev = dummy_head

    # if(temp.next != None):
    #     temp.next.prev = temp

    return head
   
updated_list = insert_middle(updated_ll, 70)
#printLL(updated_list)

#after any specific position
def insert_after_value(head, pos, value):
    dummy_head = head
    temp = Node(value)
    ct = 1
    if(pos == 1):
        return insert_first(head, value)
    while(ct < pos-1):
        dummy_head = dummy_head.next
        ct+=1
    
    temp.next = dummy_head.next
    dummy_head.next = temp
    return head


updated_linked_list = insert_after_value(updated_list, 2, 67)
printLL(updated_linked_list)
    
        

