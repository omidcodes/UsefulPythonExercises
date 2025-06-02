class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if len(haystack) < len(needle):
            return -1

        for i in range(0, len(haystack) - len(needle)  + 1):
            for j in range(0, len(needle)):
                if haystack[i+j] != needle[j]:
                    break

                if j == len(needle) - 1:
                    # last round
                    return i

        return -1
    

haystack = "mississippi"
needle = "issipi"


print(Solution().strStr(haystack, needle))