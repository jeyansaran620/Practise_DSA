def mergeAll(first,l1,second,l2):
    
    new = None
    temp3 = None
    i = 0
    j = 0
    
    while i < l1 and j < l2:
        
        if first.data < second.data:
            if temp3 == None:
                temp3 = first
                temp3.prev = None
                new = temp3
            else:
                te = temp3
                temp3.next = first
                temp3 = temp3.next
                temp3.prev = te
            first = first.next
            i += 1
            
        else:
            if temp3 == None:
                temp3 = second
                temp3.prev = None
                new = temp3
            else:
                te = temp3
                temp3.next = second
                temp3 = temp3.next
                temp3.prev = te 
            second = second.next
            j += 1
            
    while i < l1 :
        if temp3 == None:
            temp3 = first
            temp3.prev = None
            new = temp3
        else:
            te = temp3
            temp3.next = first
            temp3 = temp3.next
            temp3.prev = te
        first = first.next
        i += 1
        
    while j < l2:       
        if temp3 == None:
            temp3 = second
            temp3.prev = None
            new = temp3
        else:
            te = temp3
            temp3.next = second
            temp3 = temp3.next
            temp3.prev = te
        second = second.next
        j += 1
    
    temp3.next = None
    return new
    

def mergeSort(head,count):
    if count <= 1:
        return head
    mid = count // 2
    temp = head
    i = 0
    while i < mid:
        temp = temp.next
        i += 1
        
    first = mergeSort(head,mid)
    second = mergeSort(temp,count-mid)
    
    return mergeAll(first,mid,second,count-mid)
    

def sortDoubly(head):
    #Your code here
    temp = head
    count = 0
    while temp!= None:
        count += 1
        temp = temp.next
        
    return mergeSort(head,count)
