from .remove_duplicates_from_linked_list import LinkedList, removeDuplicatesFromLinkedList

def test_empty():
    assert removeDuplicatesFromLinkedList(None) is None

def test_single_node():
    head = LinkedList(5)
    new_head = removeDuplicatesFromLinkedList(head)

    assert head is new_head

def test_example():
    head = LinkedList(1)
    node12 = LinkedList(1)

    node31 = LinkedList(3)

    node41 = LinkedList(4)
    node42 = LinkedList(4)
    node43 = LinkedList(4)

    node51 = LinkedList(5)
    
    node61 = LinkedList(6)
    node62 = LinkedList(6)


    head.next = node12
    node12.next = node31
    node31.next = node41
    node41.next = node42
    node42.next = node43
    node43.next = node51
    node51.next = node61
    node61.next = node62

    new_head = removeDuplicatesFromLinkedList(head)

    assert new_head is head
    node = new_head.next
    assert node is node31
    node = node.next
    assert node is node41
    node = node.next
    assert node is node51
    node = node.next
    assert node is node61
    assert node.next is None
