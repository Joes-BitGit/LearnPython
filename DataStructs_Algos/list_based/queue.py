class Queue:
    """
    Queue is a fifo data structure
    Access: O(N)
    Insertion: O(1)
    Deletion: O(1)
    Search: O(N)
    Space: O(N)
    """
    def __init__(self, head=None):
        self.storage = [head]

    # Insert element
    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    # Delete element
    def dequeue(self):
        return self.storage.pop(0)
