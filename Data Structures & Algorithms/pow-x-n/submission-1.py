class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
        
        rslt = 1.0

        while n > 0:
            if n%2 == 1:
                rslt *= x
            
            x *= x
            n //= 2
        
        return rslt
