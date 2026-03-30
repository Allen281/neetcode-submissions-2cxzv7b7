class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        rslt = 0
        for i in range(32):
            aBit = 1 & a >> i
            bBit = 1 & b >> i
            finalBit = aBit^bBit^carry
            carry = aBit & bBit | aBit & carry | bBit & carry

            rslt |= finalBit << i
        
        if rslt & 0x80000000:
            return ~(rslt ^ 0xFFFFFFFF)
        return rslt & 0xFFFFFFFF