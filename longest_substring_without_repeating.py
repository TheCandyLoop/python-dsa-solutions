class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Dictionary to store last seen index
        last_seen = {}

        left = 0
        max_length = 0

        for right, char in enumerate(s):

            # If duplicate character found
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            # Update latest index
            last_seen[char] = right

            # Update maximum length
            max_length = max(max_length, right - left + 1)

        return max_length


# Example usage
obj = Solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))
