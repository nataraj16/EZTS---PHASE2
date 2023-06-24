class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlylinked:
    def __init__(self):
        self.head=None
        self.lastnode=None
    def append(self,data):
        if self.lastnode is None:
            self.head=Node(data)
            self.lastnode=self.head
        else:
            self.lastnode.next=Node(data)
            self.lastnode=self.lastnode.next
    def search(self,num):
        temp=self.head
        c=0
        while temp:
            if temp.data==num:
                print("yes node is present")
                c=1
                break
            temp = temp.next
        if(c==0):
            print("not present")

    def display(self):
        curr=self.head
        while curr is not None:
            print(curr.data,end=" ")
            curr=curr.next
a=singlylinked()
n= int(input("Enter no of nodes you want to insert: "))
for i in range(n):
    data=int(input("Enter the node"+ str(i+1)+" "))
    a.append(data)
print("The list is: ",end=" ")
a.display()
a.search(int(input("\nEnter element to search: ")))