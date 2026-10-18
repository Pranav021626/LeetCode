# Approach:
# A palindrome number reads the same forward and backward.
# For example, 121 is a palindrome, but 123 is not.
# Negative numbers are not palindromes because the minus sign
# makes the number different when reversed.
# Convert the number to a string and compare it with its reverse.
#
# Time Complexity: O(n), where n is the number of digits.
# Space Complexity: O(n), because we convert the number to a string.

class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Negative numbers cannot be palindromes.
        if x < 0:
            return False

        # Convert the number into a string.
        num = str(x)

        # Reverse the string using [::-1].
        reversed_num = num[::-1]

        # Return True if both strings are equal.
        return num == reversed_num
