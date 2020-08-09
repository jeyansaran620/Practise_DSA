def removeDuplicates(head):
    #code here
    temp=head
    prev=None
    while temp:
        if prev and prev.data==temp.data:
            prev.next=temp.next
        else:
            prev=temp
        temp=temp.next