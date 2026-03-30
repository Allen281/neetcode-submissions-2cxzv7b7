class Solution:
    def reverseBits(self, n: int) -> int:
        for i in range(16):
            lBit = n >> (31-i) & 1
            rBit = n >> i & 1

            if lBit != rBit:
                n = n ^ 1 << (31-i)
                n = n ^ 1 << i
        return n