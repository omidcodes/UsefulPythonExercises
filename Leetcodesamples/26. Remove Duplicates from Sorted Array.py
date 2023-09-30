from typing import List

_ = ""


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        output_list = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                output_list.append(nums[i])

        nums[:] = output_list[:]
        return len(output_list)


if __name__ == '__main__':
    data = [
        [([1, 1, 2]), (2, [1, 2])],
        [([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), (5, [0, 1, 2, 3, 4])],
    ]

    for entry in data:
        args = entry[0]
        expected_output = entry[1]

        # real_output = Solution().removeDuplicates(*args)
        real_output = Solution().removeDuplicates(args)
        print(real_output)

        assert real_output == expected_output, \
            f'args = `{args} / expected_output = `{expected_output}` / real_output = `{real_output}`'

    print('TESTS PASSED')
