stack=[]

def push():
    element=int(input("enter the elemen"))
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
    print(" the element are:",stack)
    
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
    elif ch==4:
        peek()
    elif ch==5:
        seek()
    else:
        break
    