class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return node(key)
    else:
        if root.val==key:
            return root
        elif root.val < key:
            root.right=insert(root.right, key)
        else:
            root.left=insert(root.left ,key)
    return root
#inorder traverse
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)
def search(root):
    n=int(input("\nelement the element to search:"))
    c=0
    while root:
        if root.val==n:
            print("\nfound")
            c=1
            break
        elif n<root.val:
            root=root.left
        else:
            root=root.right
    if c==0:
        print("not found")
        
r=node(100)
r=insert(r,70)
r=insert(r,50)
r=insert(r,60)
r=insert(r,9)
r=insert(r,-3)
r=insert(r,80)
inorder(r)
r=search(r)