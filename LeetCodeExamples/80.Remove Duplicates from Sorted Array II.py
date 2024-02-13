from typing import List

_ = ""


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        output = [nums[0]]

        last_record_repetition_count = 1

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                # new number
                output.append(nums[i])
                last_record_repetition_count = 1
                continue

            # assert nums[i - 1] == nums[i]
            if nums[i - 1] == nums[i] and last_record_repetition_count == 1:
                output.append(nums[i])
                last_record_repetition_count = 2

        nums[:] = output[:]

        return len(output), nums


if __name__ == '__main__':
    data = [
        [([1, 1, 1, 2, 2, 3]), (5, [1, 1, 2, 2, 3])],
        [([0, 0, 1, 1, 1, 1, 2, 3, 3]), (7, [0, 0, 1, 1, 2, 3, 3])],
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
