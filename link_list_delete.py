"""
This Python script defines a singly linked list and provides functionality to delete a node from the list.

The script contains:
1. A `Node` class to represent individual elements (nodes) in the linked list.
2. A `LinkedList` class to manage operations on the linked list, such as appending new nodes, deleting nodes, and printing the list.
3. The `delete_node` method in the `LinkedList` class deletes the first occurrence of a node with a specified value.
4. The `print_list` method prints the linked list in its current order.

Example:
- Original list: 1 -> 2 -> 3 -> 4 -> None
- After deleting node with value 3: 1 -> 2 -> 4 -> None
"""

# Define the Node class for a singly linked list
class Node:
    def __init__(self, data):
        self.data = data  # Assign the value to the node
        self.next = None  # Initialize the next pointer to None

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list to None

    # Method to add a new node to the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Method to delete the first occurrence of a node with a given value
    def delete_node(self, key):
        # Start at the head node
        current = self.head

        # If the head node itself holds the key to be deleted
        if current is not None:
            if current.data == key:
                self.head = current.next  # Change head to the next node
                current = None  # Free the old head node
                return

        # Search for the node to be deleted
        prev = None
        while current is not None:
            if current.data == key:
                break
            prev = current
            current = current.next

        # If the key was not present in the list
        if current is None:
            print(f"Node with value {key} not found in the list.")
            return

        # Unlink the node from the list
        prev.next = current.next
        current = None

    # Method to print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

print("Original Linked List:")
ll.print_list()

ll.delete_node(3)  # Delete node with value 3

print("Linked List after deleting node with value 3:")
ll.print_list()

ll.delete_node(5)  # Try to delete a node that doesn't exist
