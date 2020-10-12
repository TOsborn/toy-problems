class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, from_list=None):
        self.head = None
        self.tail = None

        if from_list:
            self.head = 

    def setHead(self, node):
        node.next = self.head
        self.head.prev = node
        self.head = node

    def setTail(self, node):
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def insertBefore(self, node, nodeToInsert):
        # link node.prev with nodeToInsert
        if node.prev:
            node.prev.next = nodeToInsert
            nodeToInsert.prev = node.prev

        # link nodeToInsert with node
        nodeToInsert.next = node
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # link node with nodeToInsert
        node.next = nodeToInsert
        nodeToInsert.prev = node

        # link nodeToInsert with node.next
        if node.next:
            nodeToInsert.next = node.next
            node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        node = self.head
        for _ in range(position):
            node = node.next

        self.insertBefore(node, nodeToInsert)

    def removeNodesWithValue(self, value):
        for node in self:
            if node.value == value:
                self.remove(node)

    def remove(self, node):
        # Write your code here.
        pass

    def containsNodeWithValue(self, value):
        # Write your code here.
        pass

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def to_list(self):
        as_list = []
        for node in self:
            as_list.append(node)

        return as_list

