class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curStr = ''

        for c in s:
            if c.isdigit():
                curNum = curNum*10 + int(c)
            elif c == '[':
                stack.append((curStr, curNum))
                curNum = 0
                curStr = ''
            elif c == ']':
                prev, mult = stack.pop()
                curStr = prev + (mult*curStr)
            else:
                curStr += c

        return curStr