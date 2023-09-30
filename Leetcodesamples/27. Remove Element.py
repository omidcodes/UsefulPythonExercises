from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:

        others_count: int = 0

        output_list: list = []

        for num in nums:
            if num != val:
                others_count += 1
                output_list.append(num)

        nums[:] = output_list[:]

        return others_count


if __name__ == '__main__':
    data = [
        # [([3, 2, 2, 3], 3), (2, [2, 2, "", ""])],
        [([0, 1, 2, 2, 3, 0, 4, 2], 2), (5, [0, 1, 4, 0, 3, "", "", ""])],
    ]

    for entry in data:
        args = entry[0]
        expected_output = entry[1]

        real_output = Solution().removeElement(*args)
        print(real_output)

        assert real_output == expected_output, \
            f'args = `{args} / expected_output = `{expected_output}` / real_output = `{real_output}`'

    print('TESTS PASSED')
