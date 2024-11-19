# Array like FOFI
class FIFO1:

    # Data array
    data=[]

    # Brief- Add new element to the list.
    #
    # new_val-new list element value
    #
    def Enqueue(self, new_val):
        # New element is stored on the last position
        self.data.append(new_val)
        return
    
    # Brief- Returns the first element of the list.
    #
    # No inputs
    #
    # return element value, if list has values, None otherwise
    #
    def Dequeue(self):
        # Check, if we have any elements
        if(len(self.data)==0):
            return None

        # Remove first element
        return  self.data.pop(0)
        


################################################################

## Linked list like FOFI
class FIFO2:

    # Value of element
    value=0
    # Reference to the next element
    next=None

    # Brief- Add new element to the list.
    #
    # new_val-new list element value
    #
    def Enqueue(self, new_val):

        # if the next element is not declared (which means thi is the last element in list)
        if(self.next==None):
            # we declare new ref
            self.next=FIFO2()
            # and assign new val to THIS element
            self.value=new_val
            return
        
        # if next element is declared, we know, thi is not the last
        self.next.Enqueue(new_val)
        return
    
    # Brief- Returns the first element of the list.
    #
    # No inputs
    #
    # return element value, if list has values, None otherwise
    #
    def Dequeue(self):

        # if next element is not declared, we know, that this element is not assigned, so NONE
        if(self.next==None):
            return None
        
        # If next element is declared, we save this value, and copy next element to this element
        ret=self.value
        self.value=self.next.value
        self.next=self.next.next
        return ret
################################################################
test_fifo=FIFO1()
test_fifo.Enqueue(12)
test_fifo.Enqueue(10)
test_fifo.Enqueue(2)
test_fifo.Enqueue(15)

print(test_fifo.Dequeue())
print(test_fifo.Dequeue())
print(test_fifo.Dequeue())
print(test_fifo.Dequeue())
print(test_fifo.Dequeue())

test_fifo2=FIFO2()
test_fifo2.Enqueue(13)
test_fifo2.Enqueue(8)
test_fifo2.Enqueue(25)
test_fifo2.Enqueue(16)

print(test_fifo2.Dequeue())
print(test_fifo2.Dequeue())
print(test_fifo2.Dequeue())
print(test_fifo2.Dequeue())
print(test_fifo2.Dequeue())
