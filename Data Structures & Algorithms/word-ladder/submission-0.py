class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = dict()
        wordList.append(beginWord)

        for i in range(len(wordList)):
            curWord = wordList[i]
            adj[curWord] = adj.get(curWord, list())
            for j in range(i+1, len(wordList)):
                testWord = wordList[j]
                adj[testWord] = adj.get(testWord, list())

                diffChars = 0
                for k in range(len(testWord)):
                    if curWord[k] != testWord[k]:
                        diffChars += 1
                
                if diffChars == 1:
                    adj[curWord].append(testWord)
                    adj[testWord].append(curWord)
        
        print(adj)
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

            for w in adj[word]:
                q.append((w, steps+1))

        return 0