

class Queue:
    def __init__(self):
        """ initialises the body of the queue as a list """
        self._body = []

    def __str__(self):
        retStr =""
        if len(self._body) == 0:
            return "Queue is empty"
        for item in self._body:
            retStr += "(%s, %skb) <--- " % (item._name,item._size)
        return retStr

    def enqueue(self,item):
        """ enqueues item to end of list """
        self._body.append(item)

    def dequeue(self,item):
        """ dequeues the item from the queue """
        if len(self._body) > 0 :
            for i in self._body:
                if i == item:
                    self._body.pop(self._body.index(i))
                    return item
            print("Not in queue")     
            

if __name__ == "__main__":
    
    def testQ():
        q = Queue()
        q.enqueue("a")
        q.enqueue("b")
        q.enqueue("c")
        q.enqueue("d")
        print(q)
        q.dequeue("a")
        print(q)

    testQ()