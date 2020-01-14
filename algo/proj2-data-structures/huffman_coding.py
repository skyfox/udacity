from __future__ import annotations

import heapq
from collections import Counter
from typing import Text, Dict


class Node:
    """A Node implementation of a tree. Always has left and right child."""

    def __init__(self, left: Node, right: Node) -> None:
        self.left = left
        self.right = right

    def walk(self, codemap: Text, accum: Text) -> None:
        """Walks down the tree from the current node.

        Accumulates value on the way down.

        Args:
            codemap: the Huffman code map for a given string.
            accum: currently accumulated code on the way to a leaf.
        """
        self.left.walk(codemap, accum + "0")
        self.right.walk(codemap, accum + "1")


class Leaf:
    """"A Leaf implementation if a tree. Does not have children, but hold a char."""

    def __init__(self, char: Text) -> None:
        self.char = char

    def walk(self, codemap: Dict, accum: Text):
        """Walks down the tree from the current node.

        Accumulates value on the way down.

        Args:
            codemap: the Huffman code map for a given string.
            accum: currently accumulated code on the way to a leaf.
        """
        codemap[self.char] = accum or "0"  # "0" covers the case with 1 char in a string.


def huffman_encode(string: Text) -> Dict:
    """Generates binary codes for each char based on Huffman algorithm.

    Args:
        string: the string to generate the codes for.

    Returns:
        codemap for a given string.
    """
    h = []
    # count frequencies
    for ch, freq in Counter(string).items():
        h.append((freq, len(h), Leaf(ch)))
    # and make a queue with priorities. .heappop will return the smallest element
    heapq.heapify(h)
    # counter is an artificial element of a tuple for lexicographical comparison of tuples with the same first element.
    count = len(h)
    while len(h) > 1:
        freq1, _, left = heapq.heappop(h)
        freq2, _, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        _, _, root = h.pop()
        root.walk(code, "")
    return code


def huffman_decode(encode: Text, codemap: Dict) -> Text:
    """Decodes encoded string based on provided codemap dict.

    This is straightforward greedy decoding with 2 pointers and linear time execution.

    Args:
        encode: the string to encode.
        codemap: the Huffman code map for a given string.

    Returns:
        decoded string.
    """
    decode = ""
    # Swap keys and values for faster search with 2 pointers.
    codemap = {val: key for key, val in codemap.items()}
    i, j = 0, 1
    while i < len(encode) or j < len(encode):
        if encode[i:j] in codemap:
            decode += codemap[encode[i:j]]
            i = j
        j = j + 1
    return decode


if __name__ == "__main__":
    s = "aaaabbbccd"
    code = huffman_encode(s)
    print(code)
    encode = "".join(code[ch] for ch in s)
    print(encode)
