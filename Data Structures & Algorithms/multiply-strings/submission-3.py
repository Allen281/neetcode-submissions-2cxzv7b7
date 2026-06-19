class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == 0 or num2 == 0:
            return '0'
        
        rslt = [0] * (len(num1)+len(num2))

        num1, num2 = num1[::-1], num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])

                rslt[i+j] += digit

                if rslt[i+j] > 9:
                    rslt[i+j+1] += rslt[i+j] // 10
                    rslt[i+j] %= 10
        
        rslt = rslt[::-1]

        start = 0
        for i in range(len(rslt)):
            start = i
            if rslt[i] != 0:
                break
        
        return "".join(map(str, rslt[start:]))