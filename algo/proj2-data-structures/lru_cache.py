from __future__ import annotations

from typing import Any
import math


class Node:
    """A node of a linked list."""

    def __init__(self, value: Any, prev_node: Node = None, next_node: Node = None):
        """Class constructor."""
        self.value = value
        self.prev = prev_node
        self.next = next_node

    def __repr__(self):
        return "Node[{value}]".format(value=self.value)


class DLinkedList:
    """Doubly Linked List."""

    def __init__(self, capacity=math.inf):
        self._head = None
        self._tail = None
        self._len = 0
        self._capacity = capacity

    def __len__(self):
        return self._len

    def __repr__(self):
        out = ""
        node = self._head
        while node:
            out += "Node[{value}]->".format(value=node.value)
            node = node.next
        return out

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, node: Node) -> None:
        """Inserts a node into the head."""
        # There are 3 options:
        #   1) The list is empty - directly assign the node to the head.
        if len(self) == 0:
            self._head, self._tail = node, node
            self._len += 1
        #   2) The list is not empty and is not full - set a new element as the head, current head becomes next to the head.
        else:
            self._head.prev = node
            node.next = self._head
            self._head = node
        #   3) The list is full - cut the tail.
            if len(self) + 1 > self._capacity:
                self._tail = self._tail.prev
                self._tail.next = None
            else:
                self._len += 1

    def promote_to_head(self, node) -> None:
        """Promotes the node to the head."""
        if node == self._head:
            return

        node.prev.next, node.next.prev = node.next, node.prev
        # Since we "extracted" the node from the list, we need to decrease the length of the list.
        self._len -= 1
        self.head = node


class LRUCache(object):
    def __init__(self, capacity):
        self._cache = dict()
        self._priority_list = DLinkedList()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        pass

    def set(self, key, value) -> None:
        if key not in self._cache:
            node = Node(value)
            self._priority_list.head = node
            self._cache[key] = node
        else:
            self._cache[key].value = value
            # Promote the node to the head.
            self._priority_list.promote_to_head(self._cache[key])


if __name__ == "__main__":
    l = DLinkedList(capacity=3)
    l.head = Node(10)
    l.head = Node(20)
    l.head = Node(30)
    l.head = Node(40)
