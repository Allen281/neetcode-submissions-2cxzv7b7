class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        freq = dict()
        smallest = []

        for card in hand:
            if card in freq:
                freq[card] += 1
            else:
                freq[card] = 1
                heapq.heappush(smallest, card)
        

        while smallest:
            while smallest and freq[smallest[0]] <= 0:
                heapq.heappop(smallest)
            
            if not smallest:
                break

            prev = smallest[0]
            freq[prev] -= 1

            for i in range(groupSize-1):
                cur = prev+1
                if cur not in freq or freq[cur] <= 0:
                    return False
                
                freq[cur] -= 1
                prev = cur
                
        return not smallest