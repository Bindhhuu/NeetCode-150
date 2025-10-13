class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['word'] = word
        
        rows, cols = len(board), len(board[0])
        result = set()
        
        def dfs(r, c, node):
            letter = board[r][c]
            if letter not in node:
                return
            
            nextt = node[letter]
            if 'word' in nextt:
                result.add(nextt['word'])
                del nextt['word']
            board[r][c] = '#'

            for dr, dc in[(-1,0), (1,0), (0,1), (0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, nextt)
            board[r][c] = letter

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return list(result)
        
