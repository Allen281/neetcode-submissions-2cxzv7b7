class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letterCount = [0] * 26
        expectedCount = [0] * 26

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            expectedCount[ord(s1[i]) - ord('a')] += 1
            letterCount[ord(s2[i]) - ord('a')] += 1
        
        l, r = 1, len(s1)
        while r < len(s2):
            if letterCount == expectedCount:
                return True

            letterCount[ord(s2[l-1]) - ord('a')] -= 1
            letterCount[ord(s2[r]) - ord('a')] += 1

            r += 1
            l += 1
        
        return letterCount == expectedCount

