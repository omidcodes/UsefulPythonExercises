

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        plus_one : int = int(''.join(list(map(str, digits)))) + 1
        return [int(digit) for digit in str(plus_one)]



print(Solution().plusOne([4,3,2,1]))