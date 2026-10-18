# Approach:
# Start with the first string as the common prefix.
# Compare it with every other string.
# If a string does not start with the current prefix,
# remove the last character and check again.
# Continue until the prefix matches every string or becomes empty.
#
# Time Complexity: O(n * m), where n is the number of strings
# and m is the length of the longest string.
# Space Complexity: O(m), for storing the prefix.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Use the first string as the starting prefix.
        prefix = strs[0]

        # Check the prefix against each remaining string.
        for s in strs[1:]:

            # Keep shortening the prefix until it matches the string.
            while not s.startswith(prefix):

                # Remove the last character from the prefix.
                prefix = prefix[:-1]

                # If nothing matches, return an empty string.
                if not prefix:
                    return ""

        # Return the longest prefix common to all strings.
        return prefix
