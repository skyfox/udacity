import hashlib
import unittest

from .blockchain import _Block, Blockchain


class TestBlock(unittest.TestCase):
    def test_block_hash(self) -> None:
        """Tests a block generates a content hash on init."""
        block = _Block("Test data")
        expected_result = hashlib.sha256("Test data".encode('utf-8')).hexdigest()
        self.assertEqual(expected_result, block.hash)

    def test_prev_block_hash(self) -> None:
        """Checks previous block hash setup and validity."""
        block = _Block("Test data")
        next_block = _Block("Test data 2")
        next_block.previous_block = block
        expected_result = hashlib.sha256("Test data".encode('utf-8')).hexdigest()
        self.assertEqual(expected_result, next_block.prev_hash)

    def test_empty_data(self) -> None:
        """Tests the case when data is not provided."""
        with self.assertRaises(ValueError):
            _Block("")


class TestBlockchain(unittest.TestCase):
    def test_empty_chain(self) -> None:
        """Checks when the chain is empty."""
        bc = Blockchain()
        self.assertFalse(bc.tail)

    def test_append(self) -> None:
        """Tests blockchain appending."""
        bc = Blockchain()
        block1 = _Block("Test data")
        bc.append(block1)
        block2 = _Block("Test data 2")
        bc.append(block2)
        self.assertEqual(block2, bc.tail)
        self.assertEqual(block2.previous_block, block1)
        self.assertEqual(block2.prev_hash, block1.hash)


if __name__ == '__main__':
    unittest.main()
