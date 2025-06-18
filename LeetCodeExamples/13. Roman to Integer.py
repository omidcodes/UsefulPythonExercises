class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """


        mapping = {
            'I': 1,
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M' : 1000,
        }

        output = 0

        i = 0
        while i < len(s):
            
            cur = mapping[s[i]]

            if i == len(s)-1:
                # last round
                output += cur
                return output

            next = mapping[s[i+1]]
            if cur < next:
                # e.g : IV = 5 --> 5 - 1
                output += (next - cur)
                i += 2
            else:    
                output += cur
                i += 1
        
        return output
        


assert Solution().romanToInt(s="III") == 3
assert Solution().romanToInt(s="LVIII") == 58
x = Solution().romanToInt(s="MCMXCIV") # 1994
print(x)