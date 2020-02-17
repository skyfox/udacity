import unittest

from .http_router import  RouteTrieNode, RouteTrie, Router


class TestRouteTrieNode(unittest.TestCase):
    def test_trie_node_constructor(self) -> None:
        """Tests the constructor of a route trie node."""
        default_node = RouteTrieNode()
        self.assertFalse(default_node.handler)
        self.assertFalse(default_node.children)
        custom_node = RouteTrieNode("non-empty handler")
        self.assertEqual("non-empty handler", custom_node.handler)
        self.assertFalse(custom_node.children)

    def test_node_insert(self) -> None:
        """Tests insert method."""
        node = RouteTrieNode()
        node.insert("about", "about handler")
        self.assertTrue(node.children)
        node.children["about"].insert("me")
        self.assertEqual("about handler", node.children["about"].handler)
        self.assertFalse(node.children["about"].children["me"].handler)


class TestRouteTrie(unittest.TestCase):
    def test_route_trie_constructor(self) -> None:
        """Tests the constructor of a route trie."""
        default_route_trie = RouteTrie()
        self.assertFalse(default_route_trie.root.handler)
        self.assertFalse(default_route_trie.root.children)
        custom_route_trie = RouteTrie("root handler")
        self.assertEqual("root handler", custom_route_trie.root.handler)
        self.assertFalse(custom_route_trie.root.children)

    def test_insert(self) -> None:
        """Tests insert method."""
        route_trie = RouteTrie()
        route_trie.insert(["info", "about", "me"], "about me handler")
        route_trie.insert(["info", "about"], "about handler")
        self.assertEqual("about me handler", route_trie.root.children["info"].children["about"].children["me"].handler)
        self.assertEqual("about handler", route_trie.root.children["info"].children["about"].handler)

    def test_find(self) -> None:
        """Tests find method."""
        route_trie = RouteTrie()
        route_trie.insert(["info", "about", "me"], "about me handler")
        route_trie.insert(["info", "about"], "about handler")
        self.assertFalse(route_trie.find(["info"]))
        self.assertEqual("about me handler", route_trie.find(["info", "about", "me"]))
        self.assertEqual("about handler", route_trie.find(["info", "about"]))


class TestRouter(unittest.TestCase):
    def test_router_constructor(self) -> None:
        """Tests the constructor of a router."""
        default_router = Router()
        self.assertFalse(default_router.route_trie.root.handler)
        self.assertFalse(default_router.not_found_handler)
        custom_router = Router("root handler", "not found handler")
        self.assertEqual("root handler", custom_router.route_trie.root.handler)
        self.assertEqual("not found handler", custom_router.not_found_handler)

    def test_add_handler(self) -> None:
        """Tests add handler function."""
        router = Router()
        router.add_handler("/", "root handler")
        self.assertEqual("root handler", router.route_trie.root.handler)
        router.add_handler("/about/me", "about me handler")
        self.assertEqual("about me handler", router.route_trie.root.children["about"].children["me"].handler)
        self.assertFalse(router.route_trie.root.children["about"].handler)

    def test_lookup(self) -> None:
        """Tests a typical use case."""
        router = Router("root handler", "not found handler")
        router.add_handler("/home/about", "about handler")
        self.assertEqual("root handler", router.lookup("/"))
        self.assertEqual("not found handler", router.lookup("/home"))
        self.assertEqual("about handler", router.lookup("/home/about"))
        self.assertEqual("about handler", router.lookup("/home/about/"))
        self.assertEqual("not found handler", router.lookup("/home/about/me"))


if __name__ == '__main__':
    unittest.main()
