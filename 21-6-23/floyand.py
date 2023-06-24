class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        
class Linkedlist:
    def __init__(self):
        self.head=None
        
        
    def push(self,new):
        new_node=Node(new)
        new_node.next=self.head
        self.head=new_node
            
    def detectAndRemoveloop(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        s=self.head
        f=self.head
        while(s and f and f.next):
            s=s.next
            f=f.next.next
            
                #if slow and fast meet at  some point
            if s==f:
                print("meeeting point",s.data)
                s.head=self.head    
                while (s.next!=f.next):
                    s=s.next
                    f=f.next    
                print("start of the loop",f.next.data)
                f.next=None    ##remove loop
                    
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next
o=Linkedlist()
o.head=Node(50)
o.head.next=Node(20)
o.head.next.next=Node(10)
o.head.next.next.next=Node(5)
o.head.next.next.next.next=Node(4)
extra=Node(1)
o.head.next.next.next.next.next=extra
extra.next=o.head.next
o.detectAndRemoveloop()
print(" linked list after removing loop")
o.printlist()
                    
                    