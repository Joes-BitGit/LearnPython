class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    """
    Linked list class is used to hold elements but will act as a stack.
    Which means it will delete and insert only from the top of the Stack

    """
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        # Inserting
        # Step 1 make the new_element.next point to where head is pointing to
        # Step 2 make the head point to the new_element

        # Step 1 assign head to new_element.next
        new_element.next = self.head
        # Step 2 assign the new_element to head
        self.head = new_element


    def delete_first(self):
        # Deleting
        # Step 1 Check if the LinkedList exists
        # Step 2 Assign the new head value to be the next node
        to_delete = self.head
        if self.head:
            self.head = self.head.next
            to_delete.next = None
        return to_delete

class Stack(object):
    """
    Stack is a lifo data structure
    Access: O(N)
    Insertion: O(1)
    Deletion: O(1)
    Search: O(N)
    Space: O(N)
    """
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()
