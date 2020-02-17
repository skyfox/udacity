from __future__ import annotations

from collections import defaultdict, deque
from typing import Text, Optional, List


class RouteTrieNode:
    def __init__(self, handler: Optional[Text] = None) -> None:
        """Constructs the node.

        Args:
            handler: the node handler.
        """
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler

    def __str__(self) -> Text:
        """Represents the node as a string."""
        return "Node[handler: {handler}, children: {children}]".format(
            handler=self.handler,
            children=",".join(key for key in self.children) or None)

    def insert(self, key: Text, handler: Optional[Text] = None) -> None:
        """Adds a child node.

        Args:
            key: the child node key.
            handler: the child node handler.
        """
        if key in self.children:
            self.children[key].handler = handler
        else:
            self.children[key] = RouteTrieNode(handler=handler)


class RouteTrie:
    def __init__(self, root_handler: Optional[Text] = None) -> None:
        """Constructs the route trie.

        Args:
            root_handler: handler for a root path "/".
        """
        self.root = RouteTrieNode(root_handler)

    def insert(self, path_components: List[Text], handler: Text) -> None:
        """Inserts a path to a trie.

        Args:
            path_components: path to the leaf. E.g. ["about", "me"].
            handler: leaf's handler.
        """
        node = self.root
        path_components = deque(path_components)
        while len(path_components) > 1:
            path_component = path_components.popleft()
            node = node.children[path_component]
        # Process the last element
        node.insert(path_components.pop(), handler)

    def find(self, path_components: List[Text]) -> Optional[Text]:
        """Finds the handler of the path.

        Args:
            path_components: path to the leaf. E.g. ["about", "me"].

        Returns:
            handler or None.
        """
        node = self.root
        for path_component in path_components:
            if path_component not in node.children:
                return None
            node = node.children[path_component]
        return node.handler


def split_path(path: Text) -> List[Text]:
    """Splits the path into path components.

    Args:
        path: a string path.

    Returns:
        a list of path components.
    """
    # There is no way to assign an empty handler.
    if not len(path):
        raise ValueError("Path can not be empty")
    # Do some path clean-up.
    if path[0] == "/":
        path = path[1:]
    if path[-1] == "/":
        path = path[:-1]
    return path.split("/")


class Router:
    def __init__(self, root_handler: Optional[Text] = None, not_found_handler: Optional[Text] = None) -> None:
        """Constructs a router.

        Args:
            root_handler: root handler.
            not_found_handler: not found handler.
        """
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path: Text, handler: Text) -> None:
        """Adds handler.

        Args:
            path: path to a handler.
            handler: handler name.
        """
        if path == "/":
            self.route_trie.root.handler = handler
        else:
            self.route_trie.insert(split_path(path), handler)

    def lookup(self, path: Text) -> Optional[Text]:
        """Looks up for a handler for a given path.

        Args:
            path: path to a handler.

        Returns:
            handler name for a given path or None.
        """
        handler = self.route_trie.root.handler if path == "/" else self.route_trie.find(split_path(path))
        if not handler:
            return self.not_found_handler
        return handler


if __name__ == "__main__":
    # create the router and add a route
    router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route

    # some lookups with the expected output
    assert "root handler" == router.lookup("/")
    assert "not found handler" == router.lookup("/home")
    assert "about handler" == router.lookup("/home/about")
    assert "about handler" == router.lookup("/home/about/")
    assert "not found handler" == router.lookup("/home/about/me")
