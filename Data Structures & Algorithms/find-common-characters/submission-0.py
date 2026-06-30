from collections import defaultdict
import math

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # 1. Initialize 'counts' using ONLY the first word
        counts = defaultdict(int)
        for c in words[0]:
            counts[c] += 1

        # 2. Iterate over the REST of the words
        for w in words[1:]:
            cur = defaultdict(int)
            for c in w:
                cur[c] += 1
            
            # 3. Iterate over the keys in COUNTS, not cur
            # Wrap in list() so we can safely delete keys while looping
            for k in list(counts.keys()):
                if k in cur:
                    counts[k] = min(counts[k], cur[k])
                else:
                    # If it's not in the current word, it's not a common char
                    del counts[k]
        
        rslt = list()

        for k, v in counts.items():
            for i in range(v):
                rslt.append(k)
        
        return rslt