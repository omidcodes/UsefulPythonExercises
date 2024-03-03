from typing import List


class Solution:

    def summaryRanges(self, nums: List[int]) -> List[str]:

        output = []

        head_idx = 0

        len_nums = len(nums)

        while True:
            ptr_idx = head_idx

            if head_idx > len_nums - 1:
                break

            while ptr_idx != len_nums - 1 and nums[ptr_idx + 1] == nums[ptr_idx] + 1:
                ptr_idx += 1

            if ptr_idx == head_idx:
                output.append(f"{nums[head_idx]}")
            else:
                output.append(f"{nums[head_idx]}->{nums[ptr_idx]}")

            head_idx = ptr_idx + 1

        return output


nums = [0, 2, 3, 4, 6, 8, 9]
# nums = [0, 1, 2, 4, 5, 7]

print(Solution().summaryRanges(nums=nums))
