class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie
        for i in word:
            if i not in d:
                d[i] = {}
            d = d[i]
        d['.'] = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            d = node
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for key in d:
                        if key != '.' and dfs(i + 1, d[key]):
                            return True
                    return False
                else:
                    if c not in d:
                        return False
                    d = d[c]
            return '.' in d

        return dfs(0, self.trie)

        def dfs(j, node):
            d = node
            for i in range(j, len(word)):
                c = word[i]
                if c == 

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
