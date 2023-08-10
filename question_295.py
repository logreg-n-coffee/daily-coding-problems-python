# Pascal's triangle is a triangular array of integers constructed with the following formula:
#
# The first row consists of the number 1.
# For each subsequent row, each element is the sum of the numbers directly above it, on either side.
# For example, here are the first few rows:
#
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
# Given an input k, return the kth row of Pascal's triangle.
#
# Bonus: Can you do this using only O(k) space?

from typing import List


def pascal_triangle_kth_row(n: int) -> List[int]:
    if n == 0:
        return []
    if n == 1:
        return [1]

    row: List[int] = [1]

    # using property of pascal's triangle: nCk = nC(k-1) * (n-k+1) / k
    prev_val = 1
    for i in range(1, n):
        next_val = prev_val * (n - i) // i
        row.append(next_val)
        prev_val = next_val

    return row


k: int = 5
print(f"pascal_triangle_kth_row({k}) = {pascal_triangle_kth_row(k)}")
