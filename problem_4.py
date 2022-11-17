
#Windows Active Directory, a group can consist of user(s) and group(s) themselves.

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
child2 = Group("child2")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
parent_user = "parent_user"
parent.add_user(parent_user)

child.add_group(sub_child)
parent.add_group(child)
parent.add_group(child2)

#Hierarchy:
    # G-Parent -> G-Child -> G-Sub_Child -> U-sub_child


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    #Recursion - Assume Transitive relationship

    #for user associated to each group.
    for u in group.get_users():
        if u == user:
            return True

    for sub_dir in group.get_groups():
        #Recursively call user in group's sub_directory. If condition is match, return true. If none, False
        if is_user_in_group(user,sub_dir):
            return True
    
    return False

#Test Cases

print(is_user_in_group("parent_user", parent)) #Return True
print(is_user_in_group("random_user", parent)) #Return False
print(is_user_in_group("sub_child_user", sub_child)) #Return True
print(is_user_in_group("parent_user", sub_child)) #Return False


