class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        repetition = {}

        for num in nums:

            if repetition.get(num) == 1:
                # item was seen before [This time repeated two times]
                del repetition[num]
                continue

            repetition[num] = 1
        
        # returns the only item in dict with 1 repetition
        return list(repetition.keys())[0]


nums = [1,2,4,1,2]
print(Solution().singleNumber(nums))
