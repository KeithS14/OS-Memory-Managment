

from queues import Queue
from block import Block
from process import Process
from DLL import *
class MemoryManagment:
    def __init__(self):
        self._queue = Queue()
        self._freeBlocks = FreeBlocks()
        self._b1 = Block("b0",8,None) 
        self._b2 = Block("b1",48,None)
        self._b3 = Block("b2",20,None)
        self._b4 = Block("b3",40,None)
        self._b5 = Block("b4",32,None)
        self._b6 = Block("b5",36,None)
        self._b7 = Block("b6",20,None)
        self._b8 = Block("b7",16,None)
        self._blocks = [self._b1,self._b2,self._b3,self._b4,self._b5,self._b6,self._b7,self._b8]

        for b in self._blocks:
            self._freeBlocks.addNode(b)

    def __str__(self):
        returnStr = "All Blocks:\n"
        for b in self._blocks:
            returnStr += "%s\n" % b
        return returnStr


    def memoryRequest(self,p):
        """ Deals with memory requests-
        Checks if there is free memory availible if not calls for page replacment.
        Runs best fit if there is free memory """

        if self._freeBlocks._head._next == self._freeBlocks._tail:
            if self._FIFO(p) == False:
                print("Memory is full/ No suitable block availible: Cannot allocate process %s\n"% p)
                return
        bestFit = self._bestfit(p) 
        if bestFit is not None:
            self.allocate(bestFit,p)
    
    def _bestfit(self,p):
        """ checks free blocks in linked for the block closest to the request and returns that block """
        node = self._freeBlocks._head._next 
        bestFit = None
        while node != self._freeBlocks._tail:
            if p._size <= node._block._size:
                if  bestFit == None or bestFit._block._size > node._block._size:
                    bestFit = node
            node = node._next
        return bestFit

    def allocate(self,b,p):
        """ allocates process to block.
            Enqueues block to FIFO queue and removes block from the linked list """
        i = self._blocks.index(b._block)
        self._blocks[i]._process = p 
        print("%s --> %s, %skb\n%s is no longer free\n"% (p,b._block._name,b._block._size,b._block._name))
        self._queue.enqueue(b._block)
        self._freeBlocks.removeNode(b)
        print(self._freeBlocks)
        print("FIFO queue: %s\n"%self._queue)

    def deallocate(self,block):
        """ deallocates process from block.
            adds block to linked list and dequeues block from FIFO queue """
        processFound = False
        for b in self._blocks:
            if b._name == block:
                b._process = None
                processFound = True
                print("%s is now free"% b._name)
                self._freeBlocks.addNode(b)
                self._queue.dequeue(b)
                print("%s"%self._queue)
        if processFound == False:
            print("Block not found")
            


    def _FIFO(self,p):
        """ replaces the oldest block that is big enough for the new process """
        blockFound = False
        for b in self._queue._body:
            if b._size >= p._size:
                print("%s, %skb is replacing the pages of %s in %s"%(p._pid,p._size,b._process._pid,b._name))
                b._process = p
                self._queue.enqueue(self._queue.dequeue(b))
                print(self._queue)
                blockFound = True
                return blockFound
        return blockFound

        

if __name__ == "__main__":
    def testBestFit():
        bf = MemoryManagment()
        p1 = Process("p1",8)
        p2 = Process("p2",34)
        p3 = Process("p3",20)
        p4 = Process("p4",12)
        p5 = Process("p5",45)
        p6 = Process("p6",18)
        p7 = Process("p7",27)
        p8 = Process("p8",40)
        requests = [p1,p2,p3,p4,p5,p6,p7,p8]
        print("Processes, p1 to p8 request memory\n")
        print(bf._freeBlocks)
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        for p in requests:
            bf.memoryRequest(p)
            print(bf)
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
        print("Deallocating: b7")
        bf.deallocate("b7")
        print(bf._freeBlocks)
        print(bf)
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        
        print("Deallocating: b3")
        bf.deallocate("b3")
        print(bf._freeBlocks)
        print(bf)
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        print("p9 requests memory")
        bf.memoryRequest(Process("p9",14))
        print(bf)
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        print("p10 requests memory")
        bf.memoryRequest(Process("p10",8))
        print(bf)
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        print("p11 requests memory")
        bf.memoryRequest(Process("p11",30))
        print(bf)
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("p12 requests memory")
        bf.memoryRequest(Process("p12",18))
        print(bf)
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    testBestFit()    