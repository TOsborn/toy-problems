class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedlist):
    """Remove duplicates from a sorted linked list."""
    if not linkedlist:
        return None

    head = node = linkedlist
    while node:
        while node.next and node.value == node.next.value:
            node.next = node.next.next

        node = node.next

    return head
