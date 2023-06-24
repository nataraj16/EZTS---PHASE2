class Circularqueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1
    def enqueue(self,data):
        if ((self.rear+1)%self.size==self.front):
            
            print("Queue is Full\n")
            #condition for empty
        elif (self.front==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
        else:
            self.rear = (self.rear + 1)%self.size
            self.queue[self.rear]=data
    def dequeue(self):
        if(self.front==-1):
            print("Queue is Empty\n")
        elif(self.front==self.rear):
            temp=self.queue[self.front]
            self.front=-1
            seelf.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp
    def display(self):
        if(self.front==-1):
            print("queue is empty")
        elif(self.rear>=self.front):
            print("elements in the circular queue",end=' ')
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=' ')
            print()
            
        else:
            print("element in circular Queue are:",end=' ')
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=' ')
            print()
        if ((self.rear +1)%self.size==self.front):
            print("queue is full")
a=Circularqueue(5)
a.enqueue(401)
a.enqueue(4088)
a.enqueue(408)
a.enqueue(440)
a.display()
print("Deleted value =",a.dequeue())
print("Deleted value =",a.dequeue())
a.display()
a.enqueue(88)
a.enqueue(99)
a.enqueue(100)
a.display()
a.enqueue(100)