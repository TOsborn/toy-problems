from .linked_list_construction import DoublyLinkedList, Node

# constructor
def test_constructor_multiple_nodes():
    dll = DoublyLinkedList(range(3))

    assert dll.head.value == 0
    middle = dll.head.next
    assert middle.value == 1
    assert middle.prev == dll.head
    assert middle.next == dll.tail
    assert dll.tail.value == 2

def test_constructor_empty():
    dll = DoublyLinkedList()

    assert dll.to_list() == []
    assert dll.head is dll.tail is None

def test_constructor_single_node():
    dll = DoublyLinkedList([0])
    
    assert dll.head is dll.tail
    assert dll.head.value == 0

def test_constructor_two_nodes():
    dll = DoublyLinkedList([0, 1])

    assert dll.head.value == 0
    assert dll.tail.value == 1

    assert dll.head.next is dll.tail
    assert dll.tail.prev is dll.head

# setHead
def test_setHead_on_empty():
    dll = DoublyLinkedList()
    dll.setHead(Node(0))

    assert dll == DoublyLinkedList([0])

def test_setHead_nonempty():
    dll = DoublyLinkedList([0, 1])
    dll.setHead(Node(-1))

    assert dll == DoublyLinkedList([-1, 0, 1])

# setTail
def test_setTail_on_empty():
    dll = DoublyLinkedList()
    dll.setHead(Node(0))

    assert dll == DoublyLinkedList([0])

def test_setTail_nonempty():
    dll = DoublyLinkedList([0, 1])
    dll.setTail(Node(2))

    assert dll == DoublyLinkedList([0, 1, 2])

# insertBefore
def test_insertBefore_single_node():
    dll = DoublyLinkedList([0])
    dll.insertBefore(dll.head, Node(-1))

    assert dll == DoublyLinkedList([-1, 0])

def test_insertBefore_head():
    dll = DoublyLinkedList([0, 1, 2])
    dll.insertBefore(dll.head, Node(-1))

    assert dll == DoublyLinkedList([-1, 0, 1, 2])

def test_insertBefore_node_after_head():
    dll = DoublyLinkedList([0, 2, 3])
    dll.insertBefore(dll.head.next, Node(1))

    assert dll == DoublyLinkedList([0, 1, 2, 3])

def test_insertBefore_tail():
    dll = DoublyLinkedList([0, 1, 3])
    dll.insertBefore(dll.tail, Node(2))

    assert dll == DoublyLinkedList([0, 1, 2, 3])

def test_insertBefore_middle():
    dll = DoublyLinkedList([0, 2, 3])
    dll.insertBefore(dll.head.next, Node(1))

    assert dll == DoublyLinkedList([0, 1, 2, 3])

def test_insertBefore_already_present():
    dll = DoublyLinkedList([0, 1, 2, 3])

    dll.insertBefore(dll.head, dll.head)
    assert dll == DoublyLinkedList([0, 1, 2, 3])

    dll.insertBefore(dll.head.next, dll.head)
    assert dll == DoublyLinkedList([0, 1, 2, 3])

    dll.insertBefore(dll.head.next.next, dll.head)
    assert dll == DoublyLinkedList([1, 0, 2, 3])

    dll = DoublyLinkedList([0, 1, 2, 3])
    dll.insertBefore(dll.head, dll.tail)
    assert dll == DoublyLinkedList([3, 0, 1, 2])

# insertAfter
def test_insertAfter_single_node():
    dll = DoublyLinkedList([0])
    dll.insertAfter(dll.head, Node(1))

    assert dll == DoublyLinkedList([0, 1])

def test_insertAfter_head():
    dll = DoublyLinkedList([0, 2, 3])
    dll.insertAfter(dll.head, Node(1))

    assert dll == DoublyLinkedList([0, 1, 2, 3])

def test_insertAfter_node_before_tail():
    dll = DoublyLinkedList([0, 1, 3])
    dll.insertAfter(dll.tail.prev, Node(2))

    assert dll == DoublyLinkedList([0, 1, 2, 3])

def test_insertAfter_tail():
    dll = DoublyLinkedList([0, 1, 2])
    dll.insertAfter(dll.tail, Node(3))

    assert dll == DoublyLinkedList([0, 1, 2, 3])

def test_insertAfter_middle():
    dll = DoublyLinkedList([0, 1, 3])
    dll.insertAfter(dll.head.next, Node(2))

    assert dll == DoublyLinkedList([0, 1, 2, 3])

def test_insertAfter_already_present():
    dll = DoublyLinkedList([0, 1, 2, 3])

    dll.insertAfter(dll.tail, dll.tail)
    assert dll == DoublyLinkedList([0, 1, 2, 3])

    dll.insertAfter(dll.tail.prev, dll.tail)
    assert dll == DoublyLinkedList([0, 1, 2, 3])

    dll.insertAfter(dll.head.next.next, dll.head.next)
    assert dll == DoublyLinkedList([0, 2, 1, 3])

# insertAtPosition
def test_insertAtPosition2():
    dll = DoublyLinkedList()
    dll.insertAtPosition2(0, Node(0))

    assert dll == DoublyLinkedList([0])

    dll.insertAtPosition2(2, Node(1))
    assert dll == DoublyLinkedList([0, 1])

    dll.insertAtPosition2(1, Node(-1))
    assert dll == DoublyLinkedList([-1, 0, 1])

    dll.insertAtPosition2(2, Node(2))
    assert dll == DoublyLinkedList([-1, 2, 0, 1])

    dll.insertAtPosition2(2, dll.head)
    assert dll == DoublyLinkedList([2, -1, 0, 1])

    dll.insertAtPosition2(5, Node(3))
    assert dll == DoublyLinkedList([2, -1, 0, 1, 3])

# removeNodesWithValue
def test_removeNodesWithValue():
    dll = DoublyLinkedList([0, 1, 1, 2, 1, 3])

    dll.removeNodesWithValue(-1)
    assert dll == DoublyLinkedList([0, 1, 1, 2, 1, 3])

    dll.removeNodesWithValue(1)
    assert dll == DoublyLinkedList([0, 2, 3])

    dll.removeNodesWithValue(3)
    assert dll == DoublyLinkedList([0, 2])

    dll.removeNodesWithValue(0)
    assert dll == DoublyLinkedList([2])

    dll.removeNodesWithValue(2)
    assert dll == DoublyLinkedList([])

    dll.removeNodesWithValue(0)
    assert dll == DoublyLinkedList([])

# remove
def test_remove_middle():
    dll = DoublyLinkedList([0, 1, 2, 3, 4])
    middle = dll.head.next.next # value == 2

    dll.remove(middle)

    assert dll == DoublyLinkedList([0, 1, 3, 4])

def test_remove_head():
    dll = DoublyLinkedList([0, 1, 2])
    dll.remove(dll.head)

    assert dll == DoublyLinkedList([1, 2])

def test_remove_tail():
    dll = DoublyLinkedList([0, 1, 2])
    dll.remove(dll.tail)

    assert dll == DoublyLinkedList([0, 1])

def test_remove_head_next():
    dll = DoublyLinkedList([0, 1, 2, 3])
    dll.remove(dll.head.next)

    assert dll == DoublyLinkedList([0, 2, 3])

def test_remove_tail_prev():
    dll = DoublyLinkedList([0, 1, 2, 3])
    dll.remove(dll.tail.prev)

    assert dll == DoublyLinkedList([0, 1, 3])

def test_remove_head_two_nodes():
    dll = DoublyLinkedList([0, 1])
    dll.remove(dll.head)

    assert dll.head is dll.tail
    assert dll == DoublyLinkedList([1])

def test_remove_tail_two_nodes():
    dll = DoublyLinkedList([0, 1])
    dll.remove(dll.tail)

    assert dll.head is dll.tail
    assert dll == DoublyLinkedList([0])

def test_remove_only_node():
    dll = DoublyLinkedList([0])
    dll.remove(dll.head)

    assert dll == DoublyLinkedList([])

# containsNodeWithValue
def test_containsNodeWithValue():
    dll = DoublyLinkedList([0, 1, 2])

    assert dll.containsNodeWithValue(0)
    assert dll.containsNodeWithValue(1)
    assert dll.containsNodeWithValue(2)

    assert not dll.containsNodeWithValue(3)

def test_1():
    dll = DoublyLinkedList([1, 2, 3, 4, 5])
    
    node1 = dll.head
    node2 = node1.next
    node3 = node2.next
    node4 = node3.next
    node5 = node4.next

    node3A, node3B, node6 = Node(3), Node(3), Node(6)

    assert dll == DoublyLinkedList([1, 2, 3, 4, 5])

    dll.setHead(node4)
    assert dll == DoublyLinkedList([4, 1, 2, 3, 5])

    dll.setTail(node6)
    assert dll == DoublyLinkedList([4, 1, 2, 3, 5, 6])

    dll.insertBefore(node6, node3)
    assert dll == DoublyLinkedList([4, 1, 2, 5, 3, 6])

    dll.insertAfter(node6, node3)
    assert dll == DoublyLinkedList([4, 1, 2, 5, 6, 3])

def test_2():
    node1 = Node(1)
    node2 = Node(2)

    node3 = Node(3)
    node32 = Node(3)
    node33 = Node(3)

    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    dll = DoublyLinkedList()

    dll.setHead(node5)
    assert dll == DoublyLinkedList([5])

    dll.setHead(node4)
    assert dll == DoublyLinkedList([4, 5])

    dll.setHead(node3)
    assert dll == DoublyLinkedList([3, 4, 5])

    dll.setHead(node2)
    assert dll == DoublyLinkedList([2, 3, 4, 5])

    dll.setHead(node1)
    assert dll == DoublyLinkedList([1, 2, 3, 4, 5])

    dll.setHead(node4)
    assert dll == DoublyLinkedList([4, 1, 2, 3, 5])

    dll.setTail(node6)
    assert dll == DoublyLinkedList([4, 1, 2, 3, 5, 6])

    dll.insertBefore(node6, node3)
    assert dll == DoublyLinkedList([4, 1, 2, 5, 3, 6])

    dll.insertAfter(node6, node32)
    assert dll == DoublyLinkedList([4, 1, 2, 5, 3, 6, 3])

    dll.insertAtPosition(1, node33)
    assert dll == DoublyLinkedList([3, 4, 1, 2, 5, 3, 6, 3])

    dll.removeNodesWithValue(3)
    assert dll == DoublyLinkedList([4, 1, 2, 5, 6])
    
    dll.remove(node2)
    assert dll == DoublyLinkedList([4, 1, 5, 6])

    assert dll.containsNodeWithValue(5)
