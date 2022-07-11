
class Block:
    def __init__(self, name, size, process):
        """ initialises block with a name size and process  """
        self._name = name
        self._size = size
        self._process = process

    def __str__(self):
        return "Block: %s, Size: %skb, Process: (%s)" %(self._name, self._size,self._process)
    

if __name__ == '__main__':
    b = Block("testBlock",25,None)
    print(b)