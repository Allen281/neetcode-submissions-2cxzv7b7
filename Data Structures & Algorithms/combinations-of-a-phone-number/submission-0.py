class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        rslt = list()
        letters = dict()

        letters['2'] = 'abc'
        letters['3'] = 'def'
        letters['4'] = 'ghi'
        letters['5'] = 'jkl'
        letters['6'] = 'mno'
        letters['7'] = 'pqrs'
        letters['8'] = 'tuv'
        letters['9'] = 'wxyz'

        def solve(i: int, cur: list()) -> None:
            if i == len(digits):
                if len(cur) > 0:
                    rslt.append(''.join(cur))
                return
            
            for c in letters[digits[i]]:
                cur.append(c)
                solve(i+1, cur)
                cur.pop()
        
        solve(0, [])
        return rslt