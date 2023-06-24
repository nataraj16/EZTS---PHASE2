class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
        
def printinorder(root):
    if root:
        printinorder(root.left)   #left
        print(root.val,end=' ')   #root
        printinorder(root.right)  #right

def printpreorder(root):
    if root:
        print(root.val,end=' ')   #root
        printpreorder(root.left)   #left
        printpreorder(root.right)  #right

def printpostorder(root):
    if root:
        printpostorder(root.left)       #left
        printpostorder(root.right)      #right
        print(root.val,end=' ')       #root
        
root=Node(100)
root.left=Node(400)
root.right=Node(500)
root.left.left=Node(700)
root.left.right=Node(600)
root.left.right.left=Node(900)
root.right.left=Node(800)
root.right.right=Node(200)
root.right.right.left=Node(300)
print("preorder:")
printpreorder(root)
print()
print("postorder:")
printpostorder(root)
print()
print("inorder:")
printinorder(root)
