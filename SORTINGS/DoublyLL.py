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

#empty_check
def is_empty(head):
    if(head == None):
        return True
    return False



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


#DELETIONS IN DLL

#at head
def delete_at_head(head):
    if (is_empty(head)):
        return None
    return head.next

#at tail
def delete_at_tail(head):
    dummy_head = head
    while(dummy_head.next != None):
        dummy_head = dummy_head.next
    
    dummy_head.prev.next = None
    dummy_head.prev = None
    return head

updated_list = delete_at_tail(updated_list)
#printLL(updated_list)

#delete at middle
def delete_at_middle(head):
    if(is_empty(head) or head.next == None):
        return None
    middle = length(head)//2
    if(length(head) == 2):
        return delete_at_head(head)
    dummuy_head = head
    ct=1
    while(ct < middle-1):
        ct+=1
        dummuy_head = dummuy_head.next

    dummuy_head.next = dummuy_head.next.next
    dummuy_head.next.prev = dummuy_head
    return head

updated_list1 = delete_at_middle(updated_list)
updated_list1 = delete_at_middle(updated_list1)
printLL(updated_list1)

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE-edge" />
    <meta name="viewport" content="width=device-width,initial-scale=1.0" />
    <title>My First HTML Page</title>
  </head>
  <body>
    <h5>Welcome to My Website</h5>

    <p>This is my first paragraph.</p>
    <p>
      This is my 2nd

      paragraph.
    </p>

    <h2>Formatting</h2>
    <p>
      curated and ranked based on <b>multiple factors</b>, including content
      relevancy, subject expertise, <i>posting</i> frequency, and freshness of
      content. Blogs with highest credibility within the <u>Shopping</u> space
      are ranked higher. This list is updated regularly to ensure it reflects
      the most active, influential, and valuable log<sub>2</sub> Shopping blogs
      on the internet today 2<sup>nd</sup>.
    </p>
    <address>
      <a href="mailto:jim@example.com">jim@example.com</a>

      <a href="tel:+14155550132">+1 (415) 555‑0132</a>
    </address>

    <blockquote cite="https://www.huxley.net/bnw/four.html">
      <p>
        Words can be like X-rays, if you use them properly—they'll go through
        anything. You read and you're pierced.
      </p>
    </blockquote>
    <h2>General Tags</h2>

    <div>
      <p>
        group content so it can be easily styled using the class or id
        attributes, marking a section of a document as being written in a
        different language (using the lang attribute), and so on.
      </p>
      <p>Beware of the leopard</p>
    </div>
    <p>
      Add the <span>basil</span>, <span>pine nuts</span> and
      <span>garlic</span> to a blender and blend into a paste.
    </p>
    <header>
      <h1>Main Header</h1>
    </header>
    <main>
      <article>
        <h2>Article 1</h2>
        <p>Beware of the leopard</p>
      </article>
      <article>
        <h2>Article 2</h2>
        <p>Beware of the Dogs</p>
      </article>
    </main>
    <footer>
      Portions of this content are ©1998–2026 by individual mozilla.org
      contributors. Content available under a Creative Commons license.
    </footer>
    <h1>Style and Programming Tags:</h1>
    <style></style>
    <script></script>
  </body>
</html>
 

    
        

