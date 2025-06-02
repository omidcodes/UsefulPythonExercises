class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        index_end_last_word = len(s)-1
        is_end_last_word_seen = False

        for i in range(len(s)-1 , -1 , -1): # to consider 0 itself in the loop

            if is_end_last_word_seen is False and s[i] != " ":
                is_end_last_word_seen = True
                index_end_last_word = i

            if is_end_last_word_seen and s[i] == " ":
                return index_end_last_word - i
        
        return index_end_last_word + 1

s = "   fly me   to   the modon   "
# s = "a "
# s = "abc "
print(Solution().lengthOfLastWord(s=s))
