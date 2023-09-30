from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        minimum_appearance_times: int = len(nums) // 2 + 1

        appearance_time_dict: dict = {}

        for num in nums:
            if num in appearance_time_dict.keys():
                appearance_time_dict[num] += 1
            else:
                appearance_time_dict[num] = 1

            if appearance_time_dict[num] >= minimum_appearance_times:
                return num


if __name__ == '__main__':
    data = [
        [([3, 2, 3]), (3)],
        [([2, 2, 1, 1, 1, 2, 2]), (2)],

    ]

    for entry in data:
        args = entry[0]
        expected_output = entry[1]

        # real_output = Solution().removeDuplicates(*args)
        real_output = Solution().majorityElement(args)
        print(real_output)

        assert real_output == expected_output, \
            f'args = `{args} / expected_output = `{expected_output}` / real_output = `{real_output}`'

    print('TESTS PASSED')
