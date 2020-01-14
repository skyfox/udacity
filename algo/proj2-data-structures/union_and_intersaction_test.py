import unittest

from .union_and_intersaction import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_append(self) -> None:
        """Tests the append."""
        l = LinkedList()
        l.append(10)
        l.append(20)
        l.append(30)
        self.assertEqual(10, l.head.value)
        self.assertEqual(30, l.tail.value)
        self.assertEqual(l.tail, l.head.next.next)

    def test_union(self) -> None:
        """Tests the union of 2 lists."""
        l1 = LinkedList()
        l1.append(1)
        l1.append(2)
        l1.append(3)
        l2 = LinkedList()
        l2.append(3)
        l2.append(4)
        l_union = l2.union(l1)
        self.assertEqual({1, 2, 3, 4}, l_union.values)

    def test_empty_intersection(self) -> None:
        """Tests the intersection where the result is empty."""
        l1 = LinkedList()
        l1.append(1)
        l1.append(3)
        l2 = LinkedList()
        l2.append(4)
        l2.append(2)
        l_intersection = l2.intersection(l1)
        self.assertEqual(set(), l_intersection.values)

    def test_intersection(self) -> None:
        """Tests the intersection."""
        l1 = LinkedList()
        l1.append(1)
        l1.append(2)
        l1.append(3)
        l2 = LinkedList()
        l2.append(4)
        l2.append(1)
        l2.append(2)
        l_intersection = l2.intersection(l1)
        self.assertEqual({1, 2}, l_intersection.values)


if __name__ == '__main__':
    unittest.main()
