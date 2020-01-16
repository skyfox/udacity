import unittest

from .active_directory import Group, is_user_in_group


class TestUserInGroup(unittest.TestCase):
    def setUp(self) -> None:
        self.parent = Group("parent")
        self.child = Group("child")
        sub_child_1 = Group("subchild_1")
        sub_child_2 = Group("subchild_2")

        sub_child_user = "sub_child_user"
        sub_child_1.add_user(sub_child_user)

        self.child.add_group(sub_child_1)
        self.child.add_group(sub_child_2)
        self.parent.add_group(self.child)

    def test_user_in_group(self) -> None:
        """Tests that the user is in a group"""
        self.assertTrue(is_user_in_group("sub_child_user", self.parent))
        self.assertTrue(is_user_in_group("sub_child_user", self.child))

    def test_user_not_in_group(self) -> None:
        """Tests that the user is not in a group"""
        self.assertFalse(is_user_in_group("not_a_user", self.child))

    def test_no_args(self) -> None:
        """Tests the case with default args."""
        with self.assertRaises(TypeError):
            self.assertFalse(is_user_in_group())

    def test_no_group(self) -> None:
        """Tests the case when a group instance is not provided."""
        with self.assertRaises(TypeError):
            self.assertFalse(is_user_in_group("user"))

    def test_not_group(self) -> None:
        """Tests the case when a group is not an instance of Group class."""
        with self.assertRaises(TypeError):
            self.assertFalse(is_user_in_group("user", "group"))

if __name__ == '__main__':
    unittest.main()
