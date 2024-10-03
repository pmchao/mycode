"""
This Python script defines a singly linked list and provides functionality to reverse the linked list.

The script contains:
1. A `Node` class to represent individual elements (nodes) in the linked list.
2. A `LinkedList` class to manage operations on the linked list, such as appending new nodes and reversing the list.
3. The `reverse` method in the `LinkedList` class reverses the linked list by re-arranging the `next` pointers of each node.
4. The `print_list` method prints the linked list in its current order.

How it works:
- We start by creating a linked list using the `LinkedList` class and adding nodes with data.
- The `reverse` method iteratively reverses the links between the nodes.
- The reversed list can be printed using the `print_list` method.

Example:
- Original list: 1 -> 2 -> 3 -> 4 -> None
- Reversed list: 4 -> 3 -> 2 -> 1 -> None
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

    # Method to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the link
            prev = current  # Move the previous pointer forward
            current = next_node  # Move the current pointer forward
        self.head = prev  # Set the head to the new first node

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

ll.reverse()

print("Reversed Linked List:")
ll.print_list()
