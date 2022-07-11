

class DLLNode:
    def __init__(self, item, nextnode,prevnode):
        """ initialises node with a block, next and previous node pointer   """

        self._block = item
        self._next = nextnode
        self._prev = prevnode
    
class FreeBlocks:
    def __init__(self):
        """ Initialise an empty library. """
        self._tail = DLLNode(None,None,None)
        self._head = DLLNode(None,self._tail,None)
        self._tail._prev = self._head
    
    def __str__(self):
        retStr = "Linked List - Free Blocks:\n"
        block = self._head._next
        if self._head._next == self._tail:
            return "List is empty - No Free Blocks  "

        while block != self._tail:
            retStr += "%s\n" % block._block
            block = block._next
        return retStr

    def addNode(self,block):
        """ adds block to end of the list """
        newNode = DLLNode(block,None,None)
        #if list is empty
        if self._head._next == self._tail:
            self._head._next = newNode
            newNode._next = self._tail
            self._tail._prev = newNode
            newNode._prev = self._head
        else:
            #add last 
            self._tail._block = newNode._block
            newNode = self._tail
            self._tail = DLLNode(None,None,newNode)
            newNode._next = self._tail
    
    def removeNode(self, node):
        """ removes node from list """
        node._prev._next = node._next
        node._next._prev = node._prev

        node._next = None 
        node._prev = None
        node._block = None
        
       






        






