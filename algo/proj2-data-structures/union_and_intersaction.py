from __future__ import annotations

from typing import Text


class Node:
    def __init__(self, value) -> None:
        """Class constructor.

        Args:
            value: the value of a node.
        """
        self.value = value
        self.next = None

    def __repr__(self):
        """Represents a node as a string."""
        return "Node[{value}]".format(value=self.value)


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        # Instead of wasting linear time we will waste linear memory to store
        # all unique values of a list.
        self.values = set()

    def __repr__(self) -> str:
        """Retpresents a list as a string."""
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += cur_head.__repr__() + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value: int) -> None:
        """Appends the list by a node with a given value.

        Args:
            value: the value for a new node.
        """
        self.values.add(value)
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def union(self, other: LinkedList) -> LinkedList:
        """Produces a union list of current and other.

        Args:
            other: linked list to find a union with.

        Return:
            the union of 2 linked lists.
        """
        union = LinkedList()
        for value in self.values.union(other.values):
            union.append(value)
        return union

    def intersection(self, other: LinkedList) -> LinkedList:
        """Produces a union list of current and other.

        Args:
            other: linked list to find an intersaction with.

        Return:
            the intersaction of 2 linked lists.
        """
        intersection = LinkedList()
        for value in self.values.intersection(other.values):
            intersection.append(value)
        return intersection


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(2)
    ll1.append(3)
    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(3)
    ll2.append(4)
    print(ll1.union(ll2))
    print(ll1.intersection(ll2))
