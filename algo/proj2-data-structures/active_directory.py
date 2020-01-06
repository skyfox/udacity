from __future__ import annotations

from typing import Text


class Group(object):
    def __init__(self, name: Text) -> None:
        """Class constructor.
        
        Args:
            name: a name of a group.
        """
        self.name = name
        self.groups = set()
        self.users = set()

    def add_group(self, group: Group) -> None:
        """Adds a group to a set of groups.
        
        Args:
            group: a group to add.
        """
        self.groups.add(group)

    def add_user(self, user: Text) -> None:
        """Adds a user to a list of users.
        
        Args:
            user: a user to add.
        """
        self.users.add(user)


def is_user_in_group(user: str, group: Group) -> bool:
    """Checks is a user in a group.

    Args:
      user: user name/id
      group: group to check user membership against

    Returns:
        True if user is in the group, False otherwise.
    """
    result = False
    if user in group.users:
        return True
    for inner_group in group.groups:
        result = is_user_in_group(user, inner_group)
        if result:
            break        
    return result


if __name__ == "__main__":
    parent = Group("parent")
    child = Group("child")
    sub_child_1 = Group("subchild_1")
    sub_child_2 = Group("subchild_2")

    sub_child_user = "sub_child_user"
    sub_child_1.add_user(sub_child_user)

    child.add_group(sub_child_1)
    child.add_group(sub_child_2)
    parent.add_group(child)
    print(is_user_in_group("sub_child_user", parent))
    print(is_user_in_group("sub_child_user2", parent))