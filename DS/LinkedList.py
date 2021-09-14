class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insertStart(self, data):
        self.size+=1
        newNode = Node(data)
        
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
    
    def insertEnd(self, data):
        self.size+=1
        actualNode = self.head
        newNode = Node(data)
        
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        
        actualNode.nextNode = newNode
    
    def getSize(self):
        return self.size
    
    def removeNode(self, data):
        if not self.head:
            return
        
        self.size-=1
        
        currentNode = self.head
        previousNode = None
        
        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode
        
        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode
    
    def traverse(self):
        actualNode = self.head
        while actualNode is not None:
            print(actualNode.data)
            actualNode = actualNode.nextNode

# Driver Code
linkedList = LinkedList()

linkedList.insertStart(1)
linkedList.insertStart(2)
linkedList.insertEnd(3)

print(linkedList.getSize())
linkedList.traverse()

linkedList.removeNode(2)
print(linkedList.getSize())
linkedList.traverse()