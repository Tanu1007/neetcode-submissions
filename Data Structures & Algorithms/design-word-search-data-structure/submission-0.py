class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        

    def search(self, word: str) -> bool:
        def dfs(node, word, index):
            if index == len(word):
                return node.is_end
            char = word[index]
            if char == '.':
                for child in node.children.values():
                    if dfs(child,word,index+1):
                        return True
                return False
            if char not in node.children:
                return False
            return dfs(node.children[char],word, index+1)
        return dfs(self.root, word, 0)
            
        
