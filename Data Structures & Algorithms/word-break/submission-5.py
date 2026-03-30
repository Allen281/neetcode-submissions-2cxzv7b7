class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dictionary = set()
        dp = dict()

        for word in wordDict:
            dictionary.add(word)

        def solve(i):
            if i == len(s):
                return True

            if i in dp:
                return dp[i]

            curString = ''
            for c in range(i, len(s)):
                curString += s[c]
                if curString in dictionary:
                    if solve(c+1):
                        dp[i] = True
                        return True

            dp[i] = False
            return False

        return solve(0)

        