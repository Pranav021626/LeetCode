# Approach:
# Use dynamic programming to count the number of unique BSTs.
# Assume each number can become the root of the tree.
# If a number is chosen as the root, the smaller numbers go to
# the left subtree and the larger numbers go to the right subtree.
# Multiply the possible left and right subtrees, then add the results
# for every possible root.
#
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def numTrees(self, n: int) -> int:

        # dp[i] stores the number of unique BSTs with i nodes.
        dp = [0] * (n + 1)

        # There is one empty tree and one BST with a single node.
        dp[0] = 1
        dp[1] = 1

        # Calculate the answer for every number of nodes.
        for nodes in range(2, n + 1):

            # Try every possible root.
            for root in range(1, nodes + 1):

                # Nodes smaller than the root form the left subtree.
                left = root - 1

                # Nodes larger than the root form the right subtree.
                right = nodes - root

                # Combine all possible left and right subtrees.
                dp[nodes] += dp[left] * dp[right]

        # Return the number of unique BSTs with n nodes.
        return dp[n]
