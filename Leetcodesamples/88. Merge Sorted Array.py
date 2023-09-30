from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        print(id(nums1))

        nums1_cut = nums1[:m]
        nums2_cut = nums2[:n]

        if len(nums1_cut) == 0:
            nums1[:] = nums2_cut
            return

        if len(nums2_cut) == 0:
            nums1[:] = nums1_cut
            return

        merged_output = sorted(nums1_cut + nums2_cut)

        from copy import deepcopy
        # nums1[:] = merged_output
        nums1[:] = merged_output

        print(id(nums1))

        return


if __name__ == '__main__':
    data = [
        [([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), ([1, 2, 2, 3, 5, 6])],
        # [([1], 1, [], 0), ([1])],
        # [([0], 0, [1], 1), ([1])],

    ]

    for entry in data:
        args = entry[0]
        expected_output = entry[1]

        # real_output = Solution().removeDuplicates(*args)
        real_output = Solution().merge(*args)
        print(real_output)

        assert real_output == expected_output, \
            f'args = `{args} / expected_output = `{expected_output}` / real_output = `{real_output}`'

    print('TESTS PASSED')
