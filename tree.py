class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def buildTree():
    node=Node()
    data=int(input())
    
    if data==-1:
        return None
    else:
        node.data=data
    
    node.left=buildTree()
    node.right=buildTree()
    
    return node
    
def preOrder(root):
    if not root:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.data,end=" ")
    inOrder(root.right)
    
def postOrder(root):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=' ')

def levelOrder(root):
    queue=[root]
    
    while queue:
        p=queue.pop(0)
        if p.left:
            queue.append(p.left)
        if p.right:
            queue.append(p.right)
        print(p.data)
    
    

tree=buildTree()

preOrder(tree)
levelOrder(tree)










