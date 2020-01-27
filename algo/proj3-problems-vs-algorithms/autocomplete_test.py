import unittest

from .autocomplete import TrieNode, Trie


class TestTrie(unittest.TestCase):
    def test_insert_empty(self):
        """Tests empty word insertion."""
        trie = Trie()
        trie.insert("")
        empty_word = trie.root
        self.assertFalse(empty_word.is_word)
        self.assertFalse(empty_word.children)

    def test_insert(self) -> None:
        """Tests word insertion."""
        trie = Trie()
        trie.insert("word")
        word_node = trie.root.children["w"].children["o"].children["r"].children["d"]
        self.assertTrue(word_node.is_word)
        self.assertFalse(word_node.children)

    def test_insert_almost_same(self):
        """Tests same word insertion."""
        trie = Trie()
        trie.insert("word")
        trie.insert("word1")
        trie.insert("word2")
        self.assertEqual(1, len(trie.root))
        self.assertEqual(1, len(trie.root.children["w"]))
        self.assertEqual(1, len(trie.root.children["w"].children["o"]))
        self.assertEqual(1, len(trie.root.children["w"].children["o"].children["r"]))
        self.assertEqual(2, len(trie.root.children["w"].children["o"].children["r"].children["d"]))

    def test_get_suffixes(self):
        """Tests the case when a given prefix has suffixes."""
        trie = Trie()
        words = [
            "ant", "anthology", "antagonist", "antonym",
            "fun", "function", "factory",
            "trie", "trigger", "trigonometry", "tripod"
        ]
        for word in words:
            trie.insert(word)
        suffixes = trie.get_suffixes("ant")
        self.assertEqual(['', 'hology', 'agonist', 'onym'], suffixes)
        suffixes = trie.get_suffixes("fu")
        self.assertEqual(['n', 'nction'], suffixes)

    def test_get_suffixes_empty(self):
        """Tests the case when there is no words for a given suffix."""
        trie = Trie()
        for word in ['word1', 'word2']:
            trie.insert(word)
        self.assertFalse(trie.get_suffixes('foo'))

    def test_get_all_words(self):
        """Tests the case when empty suffix was provided. Hence returns a full dict."""
        trie = Trie()
        words = [
            "ant", "anthology", "antagonist", "antonym",
            "fun", "function", "factory",
            "trie", "trigger", "trigonometry", "tripod"
        ]
        for word in words:
            trie.insert(word)
        self.assertEqual(words, trie.get_suffixes(""))


if __name__ == '__main__':
    unittest.main()
