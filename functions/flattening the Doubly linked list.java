public Node flatten(Node head) {
        Node temp = head;
        while(temp != null)
        {
            if (temp.child != null)
            {   
                Node nex = temp.next;
                
                temp.next = flatten(temp.child);
                
                if (temp.next != null)
                {
                    temp.next.prev = temp;
                }
                temp.child = null;
                Node te = temp.next;
                
                while(te.next != null)
                {
                    te = te.next;
                }
                if (nex != null)
                {
                nex.prev = te;        
                }
                te.next = nex;
            }
            temp = temp.next;
        }
        return head;
    }