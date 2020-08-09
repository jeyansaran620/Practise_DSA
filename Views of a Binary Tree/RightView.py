
def rightView(root):
    '''
    :param root: root of given tree.
    :return: print the right view of tree, dont print new line
    '''
    # code here
    if root==None:
        return
    q=deque()
    level=[]
    temp=root
    level.append(root)
    level.append('*')
    
    while len(level) > 0:
        
        node=level.pop(0)
        
        if node=='*':
            print(last.data, end=" ")
            if len(level) > 0:
                level.append('*')
        else:
        
            if node.left:
                level.append(node.left)
            
            if node.right:
                level.append(node.right)
        last=node