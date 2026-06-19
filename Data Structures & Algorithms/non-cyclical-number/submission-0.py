class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0
        used = set()

        while sum != 1:
            if n in used:
                return False
            sum = 0
            
            used.add(n)
            while n > 0:
                sum += (n%10) ** 2
                n //= 10
            
            n = sum
        
        return True

