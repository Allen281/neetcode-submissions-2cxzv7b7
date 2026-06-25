class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        wordList.append(beginWord)

        for i in range(len(wordList)):
            curWord = wordList[i]
            for j in range(len(curWord)):
                pattern = curWord[:j] + '*' + curWord[j+1:]
                adj[pattern].append(curWord)
        
        q = deque()
        q.append((beginWord, 1))
        visited = set()

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps

            if word in visited:
                continue
            visited.add(word)

            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                for p in adj[pattern]:
                    q.append((p, steps+1))

        return 0