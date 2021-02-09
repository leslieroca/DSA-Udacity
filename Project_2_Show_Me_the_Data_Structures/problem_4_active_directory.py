"""
Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy
as such. Where User is represented by str representing their ids.
"""

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Write a function that provides an efficient look up of whether the user is in a group.

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user in group.get_users():
        return True

    # Loop through all groups in the original group and pass to function "is_user_in_group" each group recursively.

    return user in group.users or any(is_user_in_group(user, sub_group) for sub_group in group.get_groups())


# Test cases
print(is_user_in_group("sub_child_user", parent))  # Prints True
print(is_user_in_group("sub_parent", parent))  # Prints False
print(is_user_in_group("", child))  # Prints False
print(is_user_in_group("sub_dogs", sub_child))  # Prints False
