class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist():
    def __init__(self):
        self.head=None
        
    def delete_begin(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        
    def delete_end(self,prev):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        
    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
        
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,'-->',end=' ')
                temp=temp.next
            #print(temp.data)
obj=Linkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(15)
n1.next=n2
n3=Node(30)
n2.next=n3
n4=Node(40)
n3.next=n4
print("the linked list:")
obj.delete_begin()
obj.delete_position(2)
obj.display()
    