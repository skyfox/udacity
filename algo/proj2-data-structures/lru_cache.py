from __future__ import annotations

from typing import Any, Hashable


class Node:
    """A node of a linked list."""

    def __init__(self, key: Hashable, value: Any, prev_node: Node = None, next_node: Node = None) -> None:
        """Class constructor.

        Args:
            key: a key of a node.
            value: a value of a node.
            prev_node: previous node.
            next_node: next node.
        """
        self.value = value
        self.key = key
        self.prev = prev_node
        self.next = next_node

    def __repr__(self) -> str:
        """Represents a node as a string value."""
        return "Node[{key}, {value}]".format(key=self.key, value=self.value)


class DLinkedList:
    """Doubly Linked List."""

    def __init__(self, capacity: int) -> None:
        """Class constructor.
        
        Args:
            capacity: the maximum number of elements a list can store.
        """
        self._head = None
        self._tail = None
        self._len = 0
        self._capacity = capacity

    def __len__(self) -> int:
        """Gets length of a list."""
        return self._len

    def __repr__(self) -> str:
        """Represents a list as a string value."""
        out = ""
        node = self._head
        while node:
            out += "Node[{key}, {value}]->".format(
                key=node.key, value=node.value)
            node = node.next
        return out

    @property
    def tail(self) -> Node:
        return self._tail

    @property
    def head(self) -> Node:
        return self._head

    @head.setter
    def head(self, node: Node) -> None:
        """Inserts a node into a head.
        
        Args:
            node: a new head node.
        """
        # There are 3 options:
        #   1) The list is empty - directly assign the node to the head.
        if len(self) == 0:
            self._head, self._tail = node, node
            self._len += 1
        #   2) The list is not empty and is not full - set a new element as the head, current 
        #      head becomes next to the head.
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

    def promote_to_head(self, node: Node) -> None:
        """Promotes the node to the head.
        
        Args:
            node: a node to be promoted as a head.
        """
        if node == self._head:
            return

        if node == self._tail:
            self._tail = self._tail.prev

        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        # Since we "extracted" the node from the list, we need to decrease the length of the list.
        self._len -= 1
        self.head = node


class LRUCache(object):
    def __init__(self, capacity) -> None:
        """Class constructor.
        
        Args:
            capacity: the maximum number of elements cache can store.
        """
        self._cache = dict()
        self._priority_list = DLinkedList(capacity)
        self._capacity = capacity
        self._len = 0

    def __len__(self) -> int:
        """Gets length of cache."""
        return self._len

    def __repr__(self) -> str:
        """Represents cache as a string value."""
        return self._cache.__repr__()

    def get(self, key: Hashable) -> Any:
        if key not in self._cache:
            # It is not OK to return -1 in general, but it is fine in scope of this task.
            return -1
        self._priority_list.promote_to_head(self._cache[key])
        return self._cache[key].value

    def set(self, key: Hashable, value: Any) -> None:
        if key not in self._cache:
            node = Node(key, value)
            if len(self) + 1 > self._capacity:  # If the cache is full
                del self._cache[self._priority_list.tail.key]
                self._len -= 1
            self._cache[key] = node
            self._priority_list.head = node
            self._len += 1
        else:
            self._cache[key].value = value
            self._priority_list.promote_to_head(self._cache[key])


if __name__ == "__main__":
    our_cache = LRUCache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache.get(1))       # returns 1
    print(our_cache.get(2))       # returns 2

    # returns -1 because 9 is not present in the cache
    print(our_cache.get(9))

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print(our_cache.get(3))
