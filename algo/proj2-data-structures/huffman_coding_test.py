import unittest
from typing import Text, Dict

from .huffman_coding import huffman_encode, huffman_decode, encode_string


class TestHuffmanEncode(unittest.TestCase):
    def test_encode_empty_line(self) -> None:
        """Tests empty line encoding."""
        s = ""
        self.assertFalse(huffman_encode(s))

    def test_encode_1(self) -> None:
        """Tests 1 char line encoding."""
        s = "a"
        result = huffman_encode(s)
        expected_result = {"a": "0"}
        self.assertDictEqual(expected_result, result)

    def test_encode_same_char(self) -> None:
        """Tests same char line encoding."""
        s = "aaaaaaaa"
        result = encode_string(s, huffman_encode(s))
        self.assertEqual("00000000", result)

    def test_encode_str(self) -> None:
        """Tests full line encoding."""
        s = "aaaabbbccd"
        result = huffman_encode(s)
        expected_result = {"a": "0", "b": "10", "c": "111", "d": "110"}
        self.assertDictEqual(expected_result, result)


class TestHuffmanDecode(unittest.TestCase):
    def test_1_char(self) -> None:
        """Checks 1-char line decoding."""
        s = "0"
        codemap = huffman_encode(s)
        bin_str = encode_string(s, codemap)
        self.assertEqual(s, huffman_decode(bin_str, codemap))

    def test_decode_str(self) -> None:
        """Checks full line decoding."""
        s = "aaaabbbccd"
        codemap = huffman_encode(s)
        bin_str = encode_string(s, codemap)
        self.assertEqual(s, huffman_decode(bin_str, codemap))


if __name__ == '__main__':
    unittest.main()
