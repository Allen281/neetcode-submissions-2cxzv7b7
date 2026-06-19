class Solution:
    def checkValidString(self, s: str) -> bool:
        left = list()
        star = list()

        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == '*':
                star.append(i)
            else:
                if not left:
                    if not star:
                        return False
                    star.pop()
                else:
                    left.pop()
        
        while left and star:
            if left[-1] > star[-1]:
                return False
            left.pop()
            star.pop()
        
        return not left