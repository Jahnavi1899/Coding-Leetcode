class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        characters = "abcdefghijklmnopqrstuvwxyz"
        wordSet = set(wordList) # for O(1) lookup of words

        queue = [beginWord]
        level = 1

        while queue:
            n = len(queue)
            for _ in range(n):
                top = queue.pop(0)

                for i in range(len(top)):
                    for ch in characters:
                        newWord = top[:i] + ch + top[i+1:]
                        print(newWord)
                        if wordSet:
                            if newWord in wordSet:
                                queue.append(newWord)
                                wordSet.remove(newWord)
                            if newWord == endWord:
                                return level + 1
                        else:
                            break
            level += 1
        return level
    
wordList = ["hot","dot","dog","lot","log","cog"]
beginWord = "hit"
endWord = "cog"

sol = Solution()
print(sol.ladderLength(beginWord, endWord, wordList))

            


        