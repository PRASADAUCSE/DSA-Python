class Node:
    """Node class for singly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None



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

def insert_after_value(head, data, value):
    dummy_head = head
    if(value == head.data): 
        return insert_first(head, data)
        
    while(dummy_head != None):
        if(dummy_head.next.data == value):
            temp = Node(data)
            temp.next = dummy_head.next
            dummy_head.next = temp
            return head
        dummy_head = dummy_head.next
    print("Value not found")
    return head
    
n1 = Node(10)
n2 = Node(20)
n3 = Node(40)

n1.next = n2
n2.next = n3



#Deletions

#at first
def delete_first(head):
    if(head == None):
        return head
    return head.next

#at last
def delete_last(head):
    if(head.next == None or head == None):
        return None
    dummy_head = head
    while(dummy_head.next.next != None):
        dummy_head = dummy_head.next
    dummy_head.next = None
    return head


#delete middle
def delete_middle(head, length):
    if(head == None or length <= 1):
        return None
    if(length == 2):
        return delete_first(head)
    count =1
    dummy_head = head
    while(count < length//2):
        dummy_head = dummy_head.next
        count+=1
    dummy_head.next = dummy_head.next.next
    return head

#is_empty function
def is_empty(head):
    if head == None:
        return True
    return False

#delete value
def delete_value(head, value):
    dummy_head = head
    if is_empty(head):
        return None
    if(head.data == value):
        return delete_first(head)
    while(dummy_head.next != None and dummy_head.next.data != value):
        dummy_head = dummy_head.next
    if(dummy_head.next != None and dummy_head.next.data == value):
        dummy_head.next = dummy_head.next.next
    else:
        print("Value not found")
    
    return head

#delete before value
def delete_before_value(head, value):
    dummy_head = head
    if(head.data == value):
        return head
    if(head.next.data == value):
        return delete_first(head)
    if is_empty(head):
        return None
    while(dummy_head.next != None and dummy_head.next.next.data != value):
        dummy_head = dummy_head.next
    if(dummy_head.next != None and dummy_head.next.next.data == value):
        dummy_head.next = dummy_head.next.next
    else:
        print("Value not found")
    return head

#delete after value
def delete_after_value(head, value):
    dummy_head = head
    if is_empty(head):
        return None
    while(dummy_head != None and dummy_head.data != value):
        dummy_head = dummy_head.next
    if(dummy_head.data == value and dummy_head != None and dummy_head.next != None):
        dummy_head.next = dummy_head.next.next
    else:
        print("Value not found to delete or no value after given value")
    return head
updated_list = delete_after_value(n1,10)
printLL(updated_list)
