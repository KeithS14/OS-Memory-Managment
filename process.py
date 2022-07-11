

class Process:
        def __init__(self, pid,size):
            """ initialises process with a process ID and size   """
            self._pid = pid
            self._size = size
        def __str__(self):
            return "PID: %s, Size: %skb" % (self._pid,self._size) 

if __name__ == "__main__":
    
    def testProcess():
        process = Process("p1",8)
        print(process)

    testProcess()