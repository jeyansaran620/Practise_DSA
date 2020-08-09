def reorderList(self):
    if (self.head==None or self.head.next==None):
        return
    # write code to reorder Nodes of Linked_List
    s=[]
    
    temp=self.head
    
    while temp:
        s.append(temp)
        
        temp=temp.next
   
    
    temp=self.head
    for i in range(0,len(s)//2):
        right=s.pop()
        
        if temp.next==right:
            temp=temp.next
        else:
            right.next=temp.next
            temp.next=right
            temp=right.next
        
    self.tail=temp
    temp.next=None
        