#!/usr/bin/python3
"""Defines the classes Node and SinglyLinkedList."""


class Node:
    """
    Class that defines a Node.

    Attributes:
        data: the data of the node.
    """
    def __init__(self, data, next_node=None):
        """Creates a new node instance.

        Args:
            __data: the data of the node.
            __next_node: the next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter of data.

        Args:
            value (int): the data of the node.

        Raises:
            TypeError: data must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Returns the next_node instance."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter of next_node.

        Args:
            value (Node): next node of a Node.

        Raises:
            TypeError: next_node must be a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class that defines a SinglyLinkedList.

    Attributes:
        head: head of the SinglyLinkedList.
    """
    def __init__(self):
        """
        Defines a new SinglyLinkedList instance.

        Args:
            __head: head of the SinglyLinkedList.
        """
        self.__head = None

    def __str__(self):
        """
        Represent the class objects as string.

        Returns: the class object represented as a string.
        """
        temp = self.__head
        x = []
        while temp:
            x.sort()
            x.append(str(temp.data))
            temp = temp.next_node

        x.sort(key=int)
        return("\n".join(x))

    def sorted_insert(self, value):
        """
        Inserts a new node in a specific position.

        Args:
            value: the data of the new node
        """
        if self.__head is None:
            new_node = Node(value)
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            new_node = Node(value)
            new_node.data = value
            new_node.next_node = self.__head
            self.__head = new_node
