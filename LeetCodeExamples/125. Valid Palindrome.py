class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_alphanumeric = ""

        for char in s:
            if char.isalnum():
                s_alphanumeric += char

        len_s_alphanumeric: int = len(s_alphanumeric)
        max_check_index: int = len_s_alphanumeric // 2
        for i in range(max_check_index):
            if s_alphanumeric[i].lower() != s_alphanumeric[len_s_alphanumeric - i - 1].lower():
                return False
        return True


m = Solution().isPalindrome(s=s)
assert Solution().isPalindrome(s=s) is True

s = "race a car"
assert Solution().isPalindrome(s=s) is False
