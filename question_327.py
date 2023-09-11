# Write a program to merge two binary trees.
# Each node in the new tree should hold a value equal to the sum of the values of the corresponding nodes of the input trees.

# If only one input tree has a node in a given position, the corresponding node in the new tree should match that input node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def merge_trees(t1, t2):
    if t1 is None and t2 is None:
        return None
    if t1 is None:
        return t2
    if t2 is None:
        return t1

    merged = TreeNode(t1.val + t2.val)
    merged.left = merge_trees(t1.left, t2.left)
    merged.right = merge_trees(t1.right, t2.right)

    return merged


def print_tree(root):
    if root is not None:
        print_tree(root.left)
        print(root.val)
        print_tree(root.right)


if __name__ == "__main__":
    # Create example trees
    #     1
    #    / \
    #   3   2
    #  /
    # 5
    tree1 = TreeNode(1)
    tree1.left = TreeNode(3)
    tree1.right = TreeNode(2)
    tree1.left.left = TreeNode(5)

    #     2
    #    / \
    #   1   3
    #    \   \
    #     4   7
    tree2 = TreeNode(2)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(3)
    tree2.left.right = TreeNode(4)
    tree2.right.right = TreeNode(7)

    # Merge trees
    #     3
    #    / \
    #   4   5
    #  / \   \
    # 5   4   7
    merged_tree = merge_trees(tree1, tree2)

    # Print the merged tree
    print_tree(merged_tree)
