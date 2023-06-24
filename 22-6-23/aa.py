stack=[]

def push():
    element=int(input("enter the size of the stack"))
    for i in range(element):
        element=int(input("element:"))
        stack.append(element)
        print(stack)
    
def pop():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element:",e)
        print(stack)
def display():
    x=int(input())
    if x==1:
        if not stack:
            print("stack is empty")
        else:
            for i in stack:
                if i%2==0:
                    print("even",i,end='')
    else:
        if not stack:
            print("stcak is empty")
        else:
            for i in stack:
                if i%2!=0:
                    print("odd",i)
    
def peek():
    if not stack:
        print("stack is empty")
    else:
        print(stack[-1])
        
def seek():
    if not stack:
        print("stack is empty")
    else:
        n=int(input("enter the element to be search"))
        if n not in stack:
            print("not found")
        else:
            print("found")
    
while True:
    print("\nselect the options 1.push 2.pop 3.display 4.peek 5.seek 6.exit")
    ch=int(input())
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        display()
    else:
        break
    
