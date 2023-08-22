# Given a binary search tree, find the floor and ceiling of a given integer.
# The floor is the highest element in the tree less than or equal to an integer,
# while the ceiling is the lowest element in the tree greater than or equal to an integer.

# If either value does not exist, return None.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_floor_ceiling(root, x):
    floor, ceiling = None, None

    while root:
        # if root is equal to x, then floor and ceiling are both x
        if root.val == x:
            return root.val, root.val
        # if root is greater than x, then ceiling is root and floor is in left subtree
        elif root.val > x:
            ceiling = root.val
            root = root.left
        # if root is less than x, then floor is root and ceiling is in right subtree
        else:
            floor = root.val
            root = root.right

    return floor, ceiling


if __name__ == '__main__':
    root = TreeNode(8, TreeNode(4, TreeNode(2), TreeNode(6)),
                    TreeNode(12, TreeNode(10), TreeNode(14)))
    x = 7
    floor_val, ceiling_val = find_floor_ceiling(root, x)
    print(f"Floor: {floor_val}, Ceiling: {ceiling_val}")
