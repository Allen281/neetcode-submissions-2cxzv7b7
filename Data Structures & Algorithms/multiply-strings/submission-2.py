class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def strToNum(sNum: str) -> int:
            rslt = 0

            for c in sNum:
                rslt *= 10
                rslt += ord(c) - ord('0')
            
            return rslt
        
        def numToStr(num: int) -> str:
            rslt = ''

            while num > 0:
                rslt += str(num%10)
                num //= 10
            
            return rslt[::-1] if len(rslt) > 0 else '0'

        return numToStr(strToNum(num1) * strToNum(num2))