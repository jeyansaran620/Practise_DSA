def bottomView(root):
    '''
    :param root: root of the binary tree
    :return: None, Bottom view
    '''
    
    # code here
    if root==None:
        return
    q=deque()
    level=[]
    levelValues={}
    temp=root
    level.append([root,0])
    
    while(len(level) > 0):
        
        node,hd=level.pop(0)
        
        if levelValues.get(hd):
            levelValues[hd].append(node.data)
        else:
            levelValues[hd]=[node.data]
        
        if node.left:
            level.append([node.left,hd-1])
            
        if node.right:
            level.append([node.right,hd+1])
    
    for x in sorted(levelValues):
        print(levelValues[x][0], end=" ")
