class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric characters
        filtered = ''.join(c for c in s if c.isalnum())
        #print(f"Filtered string: {filtered}")  # Debugging step

        # Convert to lowercase
        filtered = filtered.lower()
        #print(f"Lowercase string: {filtered}")  # Debugging step

        # Check if it's a palindrome
        return filtered == filtered[::-1]