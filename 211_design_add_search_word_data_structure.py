class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        return self.dfs(0, word, self.root)

    def dfs(self, idx, word, root):
        curr = root
        for i in range(idx, len(word)):
            if word[i] != "." and word[i] not in curr.children:
                return False
            if word[i] == ".":
                for key in curr.children:
                    if self.dfs(i+1, word, curr.children[key]):
                        return True
            else:
                curr = curr.children[word[i]]
        return curr.endOfWord

["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
[[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('a')
obj.addWord('a')
# obj.addWord('mad')
# print(obj.search('.'))
# print(obj.search('a'))
# print(obj.search('aa'))
# print(obj.search('a'))
print(obj.search('.a'))
print(obj.search('a.'))