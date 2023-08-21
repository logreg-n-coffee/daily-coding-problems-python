# Given a linked list, remove all consecutive nodes that sum to zero.
# Print out the remaining nodes.

# For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6.
# In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.

class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_nodes(ll):
    start = ll

    while start:
        end = start
        total = 0
        skip_until = None  # this node will be used to skip the sequence that sums to zero

        # Search for a zero-sum sequence starting from `start`
        while end:
            total += end.value
            if total == 0:
                skip_until = end
                break
            end = end.next

        # If a zero-sum sequence is found, we skip printing that sequence
        if skip_until:
            start = skip_until.next
        else:
            print(start.value)
            start = start.next


# Test
# Construct linked list: 3 -> 4 -> -7 -> 5 -> -6 -> 6
ll = LinkedList(3, LinkedList(
    4, LinkedList(-7, LinkedList(5, LinkedList(-6, LinkedList(6))))))

print_nodes(ll)
