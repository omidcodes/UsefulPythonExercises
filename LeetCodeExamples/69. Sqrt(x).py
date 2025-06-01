class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0 or x == 1:
            return x

        low = 1
        high = x
        
        while True:
            
            if high == low + 1 :
                return low
            
            mid = (low + high) // 2        

            mid_pow_2 = mid * mid

            if mid_pow_2 == x:
                return mid
            
            if mid_pow_2 > x:
                # low does not change
                high = mid
            elif mid_pow_2 < x:
                low = mid



print(Solution().mySqrt(2147395599))
# print(Solution().mySqrt(2))