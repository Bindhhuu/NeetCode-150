from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    
        wordSet = set(wordList)  
        if endWord not in wordSet:
            return 0  

        queue = deque()
        queue.append((beginWord, 1))  

        while queue:
            word, steps = queue.popleft()

            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + ch + word[i+1:]

                    if newWord == endWord:
                        return steps + 1  

                    if newWord in wordSet:
                        queue.append((newWord, steps + 1))
                        wordSet.remove(newWord)  

        return 0  
