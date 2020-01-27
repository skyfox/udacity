from collections import defaultdict
from typing import Text, List


class TrieNode:
    """Defaultdict-based trie node implementation."""
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.is_word = False

    def __len__(self):
        return len(self.children)

    def suffixes(self, suffixes: List[Text], suffix: Text = "") -> None:
        """Gets all suffixes of the current node.

        The property of the suffix end - it is the ford.

        Args:
            suffixes: the list to accumulate words suffixes.
            suffix: current word suffix.
        """
        # Base of the recursion - given node represents a word.
        if self.is_word:
            # 'suffixes' will be passed by reference. Hence we can safely add a suffix.
            suffixes.append(suffix)
        # Recursion body - call suffixes() for each child.
        for child_char in self.children:
            # find suffixes for each child of the current node.
            self.children[child_char].suffixes(suffixes, suffix + child_char)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: Text) -> None:
        """Inserts a word into the trie.

        Args:
            word: a word to add to the trie.
        """
        if not word:
            return

        node = self.root
        for char in word:
            node = node.children[char]
        node.is_word = True

    def get_suffixes(self, prefix: Text) -> List[Text]:
        """Gets all prefixes for a given suffix.

        Args:
            prefix: a prefix to match.

        Returns:
            a list of suffixes of a given prefix.
        """
        node = self.root
        # Get the sub-tree based on a given prefix
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        suffixes = []
        # Pass 'suffixes' list by reference to recursive calls.
        node.suffixes(suffixes)
        return suffixes


if __name__ == "__main__":
    trie = Trie()
    words = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in words:
        trie.insert(word)
    print(trie.get_suffixes("anthology"))
