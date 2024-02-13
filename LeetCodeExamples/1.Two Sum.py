from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


if __name__ == '__main__':
    data = [
        [([2, 7, 11, 15], 9), [0, 1]],
        [([3, 2, 4], 6), [1, 2]],
        [([3, 3], 6), [0, 1]],

    ]

    for entry in data:
        args = entry[0]
        expected_output = entry[1]

        real_output = Solution().twoSum(*args)
        # print(real_output)

        assert real_output == expected_output, \
            f'args = `{args} / expected_output = `{expected_output}` / real_output = `{real_output}`'

    print('TESTS PASSED')
