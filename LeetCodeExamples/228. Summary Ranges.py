# TODO : FIX me ...

# from typing import List
#
#
# class Solution:
#
#     def summaryRanges(self, nums: List[int]) -> List[str]:
#
#         output = []
#
#         i = 0
#         while True:
#
#             if i == len(nums) - 1:
#                 # The last one
#                 output.append(f"{nums[i]}")
#                 break
#
#             for j in range(i, len(nums)):
#                 if nums[j] != nums[j - 1] + 1:
#                     if i == j - 1:
#                         output.append(f"{nums[i]}")
#                     else:
#                         output.append(f"{nums[i]}->{nums[j]}")
#
#                     i = j + 1
#
#                     break
#
#         return output
#
#
# nums = [0, 2, 3, 4, 6, 8, 9]
#
# print(Solution().summaryRanges(nums=nums))
