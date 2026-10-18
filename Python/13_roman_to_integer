# Approach:
# Store the value of each Roman numeral in a dictionary.
# Usually, we add the value of each symbol to the total.
# But when a smaller value comes before a larger value,
# subtract the smaller value instead.
# For example, IV means 5 - 1 = 4.
#
# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(1), because the dictionary has a fixed number of symbols.

class Solution:
    def romanToInt(self, s: str) -> int:

        # Map each Roman numeral to its integer value.
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Store the final integer value.
        total = 0

        # Visit each Roman numeral.
        for i in range(len(s)):

            # Check whether a next character exists and
            # whether the current value is smaller than the next.
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:

                # Subtract when a smaller numeral comes before a larger one.
                total -= values[s[i]]

            else:
                # Otherwise, add the current numeral's value.
                total += values[s[i]]

        # Return the converted integer.
        return total
