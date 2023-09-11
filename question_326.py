# A Cartesian tree with sequence S is a binary tree defined by the following two properties:

# It is heap-ordered, so that each parent value is strictly less than that of its children.
# An in-order traversal of the tree produces nodes with values that correspond exactly to S.
# For example, given the sequence [3, 2, 6, 1, 9], the resulting Cartesian tree would be:

#       1
#     /   \
#   2       9
#  / \
# 3   6
# Given a sequence S, construct the corresponding Cartesian tree.

# One simple way to construct a Cartesian tree is to iterate through the sequence S, maintaining a stack.
# The stack contains the nodes yet to be processed, and it is maintained in decreasing order.
#
# The basic idea is as follows:

# Initialize an empty stack.
# For each element x in S:

# While the stack is not empty and the top element of the stack is greater than x, pop the stack.
# Make the last popped item (if any) the left child of x.
# Make the new top item of the stack (if any) the right child of x.
# Push x onto the stack.


class Node:
    def __init__(self, val):
        self.val = val
        self.left: None | Node = None
        self.right: None | Node = None


def build_cartesian_tree(seq):
    stack = []
    root = None

    for x in seq:
        new_node = Node(x)
        last_popped = None

        while stack and stack[-1].val > x:
            last_popped = stack.pop()

        if last_popped:
            new_node.left = last_popped

        if stack:
            stack[-1].right = new_node

        stack.append(new_node)

        if not root or root.val > new_node.val:
            root = new_node

    return root


def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


if __name__ == "__main__":
    seq = [3, 2, 6, 1, 9]
    root = build_cartesian_tree(seq)

    print(inorder_traversal(root))
