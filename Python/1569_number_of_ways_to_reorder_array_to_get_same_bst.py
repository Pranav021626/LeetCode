# Approach:
# The first number becomes the root of the Binary Search Tree (BST).
# Smaller numbers go to the left subtree, and larger numbers go
# to the right subtree.
#
# We can rearrange the remaining numbers as long as the numbers
# going left and right keep their relative order.
# Use combinations to count the ways to place the left and right
# subtree numbers, then multiply by the ways to arrange each subtree.
#
# Finally, subtract 1 because the original array is not counted
# as a different reordering.
#
# Time Complexity: O(n^2) in the worst case.
# Space Complexity: O(n^2) in the worst case due to recursive sublists.

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute factorials to calculate combinations efficiently.
        fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        # Precompute inverse factorials using modular arithmetic.
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        # Calculate the number of ways to choose r items from n items.
        def comb(n, r):
            return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

        # Count the valid reorderings that produce the same BST.
        def count_ways(arr):

            # An empty tree or a tree with one or two nodes
            # has only one possible ordering for this purpose.
            if len(arr) <= 2:
                return 1

            # The first number is the root of the BST.
            root = arr[0]

            # Smaller numbers belong to the left subtree.
            left = [x for x in arr if x < root]

            # Larger numbers belong to the right subtree.
            right = [x for x in arr if x > root]

            # Choose positions for the left subtree numbers.
            # The remaining positions are used by the right subtree.
            ways_to_place = comb(len(arr) - 1, len(left))

            # Count valid reorderings for both subtrees.
            left_ways = count_ways(left)
            right_ways = count_ways(right)

            # Combine the choices and apply modulo.
            return (
                ways_to_place * left_ways * right_ways
            ) % MOD

        # Subtract one to exclude the original ordering.
        return (count_ways(nums) - 1) % MOD
