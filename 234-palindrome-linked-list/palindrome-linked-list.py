class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        current = head

        while current:
            stack.append(current.val)
            current = current.next

        current = head

        while current:
            if current.val != stack.pop():
                return False
            current = current.next

        return True