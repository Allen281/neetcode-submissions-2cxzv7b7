class FreqStack:

    def __init__(self):
        self.maxFreq = 0
        self.freq = defaultdict(int)
        self.stacks = defaultdict(list)

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.stacks[self.freq[val]].append(val)

        if self.freq[val] > self.maxFreq:
            self.maxFreq = self.freq[val]

    def pop(self) -> int:
        val = self.stacks[self.maxFreq][-1]
        self.stacks[self.maxFreq].pop()
        if not self.stacks[self.maxFreq]:
            self.maxFreq -= 1
        
        self.freq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()