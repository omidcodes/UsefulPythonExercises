from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        minimum_appearance_times: int = len(nums) // 2 + 1

        unique_numbers: list = list(set(nums))

        for unique_number in unique_numbers:
            if nums.count(unique_number) >= minimum_appearance_times:
                return unique_number


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
