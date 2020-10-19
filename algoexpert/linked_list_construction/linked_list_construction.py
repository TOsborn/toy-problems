class Node:
    """Node class for use in a doubly-linked list."""
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        prev_val = None if self.prev is None else self.prev.value
        next_val = None if self.next is None else self.next.value
        return f"({prev_val}<{self.value}>{next_val})"

    def __eq__(self, other):
        self_prev_val = None if self.prev is None else self.prev.value
        self_next_val = None if self.next is None else self.next.value

        other_prev_val = None if other.prev is None else other.prev.value
        other_next_val = None if other.next is None else other.next.value

        value_eq = (self.value == other.value)
        prev_eq = (self_prev_val == other_prev_val)
        next_eq = (self_next_val == other_next_val)

        return value_eq and prev_eq and next_eq



class DoublyLinkedList:
    """Doubly-linked list class.
    
    Supports efficient insertion and removal of nodes.
    """
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        if data:
            for value in data:
                self.setTail(Node(value))

    def setHead(self, node):
        """Insert a node in the head position.

        If the node already appears in the list, it is moved to the
        head position.
        """
        if node in self:
            self.remove(node)

        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = self.tail = node

    def setTail(self, node):
        """Insert a node in the tail position.

        If the node already appears in the list, it is moved to the
        tail position.
        """
        if node in self:
            self.remove(node)

        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = self.tail = node

    def insertBefore(self, node, nodeToInsert):
        """Insert a node immediately before a given node.

        If the node to insert already appears in the list, it is moved
        to the new position.
        """
        if node is nodeToInsert:
            return
        
        if nodeToInsert in self:
            self.remove(nodeToInsert)
        
        if node is self.head:
            self.setHead(nodeToInsert)
        else:
            # link node.prev with nodeToInsert
            if node.prev:
                node.prev.next = nodeToInsert
                nodeToInsert.prev = node.prev

            # link nodeToInsert with node
            nodeToInsert.next = node
            node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        """Insert a node immediately after a given nodee.

        If the node to insert already appears in the list, it is moved
        to the new position.
        """
        if node is nodeToInsert:
            return

        if nodeToInsert in self:
            self.remove(nodeToInsert)
        
        if node is self.tail:
            self.setTail(nodeToInsert)
        else:
            # link node with nodeToInsert
            nxt = node.next
            node.next = nodeToInsert
            nodeToInsert.prev = node

            # link nodeToInsert with node.next
            if nxt:
                nodeToInsert.next = nxt
                nxt.prev = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        """Insert a node at a given index.
        
        If the node to insert already appears in the list, it is moved
        to the new position.

        Note: If the node already appears in the list, and in
        particular if the node appears before the given insertion
        point, this method inserts the node at what would be the given
        position if the node were still at its original position. I 
        view this functionality as incorrect and have included a 
        separate method, insertAtPosition2, which always results in the
        inserted node appearing at the given position.
        """
        if position == 1:
            self.setHead(nodeToInsert)
        else:
            node = self.head
            for _ in range(position-2):
                node = node.next

            if nodeToInsert in self:
                if nodeToInsert is node:
                    return
                else:
                    self.remove(nodeToInsert)

            self.insertAfter(node, nodeToInsert)
    
    def insertAtPosition2(self, position, nodeToInsert):
        """Insert a node at a given index.
        
        If the node to insert already appears in the list, it is moved
        to the new position.

        This method is an alternative to insertAtPosition which always
        results in the node appearing at the given position in the
        modified list.
        """
        if nodeToInsert in self:
            self.remove(nodeToInsert)
        
        if position == 1:
            self.setHead(nodeToInsert)
        else:
            node = self.head
            for _ in range(position-2):
                node = node.next

            self.insertAfter(node, nodeToInsert)

    def removeNodesWithValue(self, value):
        """Remove all nodes containing a given value."""
        to_remove = []
        for node in self:
            if node.value == value:
                to_remove.append(node)

        for node in to_remove:
            self.remove(node)

    def remove(self, node):
        """Remove a given node.
        
        Requires that the node be present in the list.
        """
        assert node in self
        if node is self.head:
            if self.head is self.tail:
                self.head = self.tail = None
            else:
                self.head = node.next
                self.head.prev = None
        elif node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.prev = node.next = None

    def containsNodeWithValue(self, value):
        """Check whether list contains a node with a given value."""
        for node in self:
            if node.value == value:
                return True
        
        return False

    def to_list(self):
        """Create a python type list of values."""
        return [node.value for node in self]

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __contains__(self, node):
        for node2 in self:
            if node2 is node:
                return True

        return False

    def __len__(self):
        return len(iter(self))

    def __bool__(self):
        return self.head is not None

    def __repr__(self):
        return repr(list(self))

    def __eq__(self, other):
        return list(self) == list(other)
