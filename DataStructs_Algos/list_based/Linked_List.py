class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
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

    def get_position(self, position):
        # Get the position
        # Use a for loop starting from index 1 until you reach your position
        # if that position does not exist it means that none is hit before the loop could end

        # Start from the beginning of linked list
        current = self.head
        # Check the postion
        for i in range(1, position):
            # Traverse the LinkedList until we reach the position
            if current.next:
                current = current.next
            # if we get to the end of the LinkedList before reaching the position then return none
            else:
                return None
        # Once the for loop is finished that means the position was found before the end
        return current

    def insert(self, new_element, position - 1):
        # To insert
        # First connect the new_element to the current.next
        # Second connect the current to the new_element
        # Third delete the connection from current to current.next
        current = self.head

        for i in range(1, position):
            prev = current
            if current.next:
                current = current.next

        if prev:
            new_element.next = current
            prev.next = new_element
        else:
            new_element.next = current
        pass

    def delete(self, value):
        # Deletion
        # Traverse the LinkedList search for the self.value
        # Set the next of the current node to the prev.next
        # Assign the prev to be the new current
        current = self.head

        if current.value == value:
            self.head = current.next
        else:
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                current = current.next

        pass
