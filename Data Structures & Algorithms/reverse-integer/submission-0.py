class Solution:
    def reverse(self, x: int) -> int:
        UPPER_BOUND = 2**31 - 1
        LOWER_BOUND = 2**31

        rslt = 0
        isNeg = x < 0
        x = abs(x)

        while x > 0:
            digit = x%10
            print(digit)

            if not isNeg and (UPPER_BOUND-digit) / 10 < rslt:
                return 0

            if isNeg and (LOWER_BOUND-digit) / 10 < rslt:
                return 0
            
            rslt = rslt*10 + digit
            x //= 10
        
        return -rslt if isNeg else rslt