import unittest

from .lru_cache import Node, _DLinkedList, LRUCache


class TestNode(unittest.TestCase):
    """Test case for Node class."""

    def test_str_repr(self):
        """Tests how the Node will be printed as a string."""
        node = Node("key", "value")
        self.assertEqual("Node[key, value]", node.__repr__())


class TestDLinkedList(unittest.TestCase):
    """Test case for Doubly Linked List class."""

    def test_str_repr(self):
        """Tests how the list will be printed as a string."""
        node = Node("key", "value")
        llist = _DLinkedList(10)
        llist.head = node
        self.assertEqual("Node[key, value]->", llist.__repr__())

    def test_list_len(self):
        """Tests the length counter of the list."""
        llist = _DLinkedList(10)
        self.assertEqual(0, len(llist))
        llist.head = Node("key1", "value1")
        self.assertEqual(1, len(llist))
        llist.head = Node("key2", "value2")
        self.assertEqual(2, len(llist))

    def test_get_set_head_tail(self):
        """Tests head and tail getters"""
        llist = _DLinkedList(10)
        node1 = Node("key1", "value1")
        llist.head = node1
        node2 = Node("key2", "value2")
        llist.head = node2
        node3 = Node("key3", "value3")
        llist.head = node3
        self.assertEqual(llist.head, node3)
        self.assertEqual(llist.tail, node1)

    def test_set_head_overflow(self):
        """Tests head setter the list is full."""
        llist = _DLinkedList(3)
        # Node[key1, value1] will be evicted from the list because capacity=3
        llist.head = Node("key1", "value1")
        tail_node = Node("key2", "value2")
        llist.head = tail_node
        llist.head = Node("key3", "value3")
        head_node = Node("key4", "value4")
        llist.head = head_node
        self.assertEqual(tail_node, llist.tail)
        self.assertEqual(head_node, llist.head)

    def test_promote_to_head(self):
        llist = _DLinkedList(3)
        node1 = Node("key1", "value1")
        llist.head = node1
        llist.head = Node("key2", "value2")
        llist.head = Node("key3", "value3")
        llist.promote_to_head(node1)
        self.assertEqual(node1, llist.head)


class TestLRUCache(unittest.TestCase):
    """Tests LRU Cache class."""

    def setUp(self) -> None:
        self.lru_cache = LRUCache(5)
        self.lru_cache.set(1, 1)
        self.lru_cache.set(2, 2)
        self.lru_cache.set(3, 3)
        self.lru_cache.set(4, 4)

    def test_len(self):
        """Tests the length counter of the list."""
        self.assertEqual(4, len(self.lru_cache))

    def test_key_present(self):
        """Tests correct return for the existing key."""
        self.assertEqual(1, self.lru_cache.get(1))
        self.assertEqual(2, self.lru_cache.get(2))

    def test_key_not_present(self):
        """Tests correct return for non-existing key."""
        self.assertEqual(-1, self.lru_cache.get(9))

    def test_cache_eviction(self):
        """Tests that the cache loses some entities when out of capacity."""
        self.lru_cache.get(1)
        self.lru_cache.get(2)
        self.lru_cache.set(5, 5)
        self.lru_cache.set(6, 6)
        self.assertEqual(-1, self.lru_cache.get(3))

    def test_zero_capacity(self):
        """Tests instantiating LRU cache with 0 capacity."""
        with self.assertRaises(ValueError):
            LRUCache(0)

    def test_update_value(self):
        self.lru_cache.set(4, 42)
        self.assertEqual(42, self.lru_cache.get(4))


if __name__ == '__main__':
    unittest.main()
