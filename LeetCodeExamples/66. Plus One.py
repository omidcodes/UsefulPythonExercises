# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """

#         plus_one : int = int(''.join(list(map(str, digits)))) + 1
#         return [int(digit) for digit in str(plus_one)]


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        #  e.g: 999 ->  If all digits are 9, prepend 1 to the list
        return [1] + digits
    

print(Solution().plusOne([4,3,2,1]))    # 4 3 2 2
print(Solution().plusOne([2,9,9]))  # 300
print(Solution().plusOne([9, 9 , 9 ,9]))  # 300
print(Solution().plusOne([9]))  # 10
print(Solution().plusOne([0]))  # 1