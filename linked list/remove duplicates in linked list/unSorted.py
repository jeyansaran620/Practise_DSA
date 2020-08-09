def removeDuplicates(head):
    #code here
    values=set()
    temp=head
    prev=None
    while temp:
        if prev and temp.data in values:
            prev.next=temp.next
        else:
            values.add(temp.data)
            prev=temp
        temp=temp.next
    return head