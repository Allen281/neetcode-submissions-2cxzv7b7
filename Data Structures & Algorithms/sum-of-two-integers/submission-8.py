class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b & 0xFFFFFFFF != 0:
            carry = (a&b) << 1
            a = a ^ b
            b = carry
        a = a & 0xFFFFFFFF
        return ~(a ^ 0xFFFFFFFF) if a >= 0x80000000 else a
