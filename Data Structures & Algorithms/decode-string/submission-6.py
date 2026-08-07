class Solution:
    def decodeString(self, s: str) -> str:
        parsed = [x for x in re.split(r'(\d+)|([\[\]])', s) if x]
        nums = []
        letters = []
        for p in parsed:
            if p.isdigit():
                nums.append(int(p))
            elif p == ']':
                mult = nums.pop()
                rslt = mult*letters.pop()

                if letters:
                    letters.pop()
                if letters and letters[-1].isalpha():
                    letters[-1] += rslt
                else:
                    letters.append(rslt)
            else:
                if p.isalpha() and letters and letters[-1] != '[':
                    letters[-1] += p
                else:
                    letters.append(p)
        
        return letters[0]
