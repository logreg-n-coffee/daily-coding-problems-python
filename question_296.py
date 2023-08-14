# Given a sorted array, convert it into a height-balanced binary search tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(nums):
    if not nums:
        return None

    mid = len(nums) // 2

    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid + 1:])

    return root


# a helper tool to print level order traversal of a tree
def print_level_order(root):
    if not root:
        return

    result = []
    queue = [root]

    while queue:
        level = []
        level_size = len(queue)

        for _ in range(level_size):
            current_node = queue.pop(0)
            level.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        result.append(level)

    print(result)


# Test
nums = [-10, -3, 0, 5, 9]
root = sorted_array_to_bst(nums)
print_level_order(root)

nums = [-10, -7, -5, -3, 0, 5, 9, 10, 15, 20]
root = sorted_array_to_bst(nums)
print_level_order(root)
