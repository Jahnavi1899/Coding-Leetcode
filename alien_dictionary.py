from collections import deque

class Solution:
    def alienOrder(self, words) -> str:
        hashmap = {c : [] for word in words for c in word}
        indegree = {c : 0 for word in words for c in word}
        queue = deque()
        res = ""

        for i in range(len(words)-1):
            curr = words[i]
            nxt = words[i+1]
            n = min(len(curr), len(nxt))

            for j in range(n):
                if curr[j] != nxt[j]:
                    hashmap[curr[j]].append(nxt[j])
                    break
            if len(curr) > len(nxt) and curr[:n] == nxt:
                return ""

        numchars = len(hashmap)

        for k, v in hashmap.items():
            for adj in v:
                indegree[adj] += 1

        for k, v in indegree.items():
            if v == 0:
                queue.append(k)

        while queue:
            top = queue.popleft()
            res += top

            for adj in hashmap[top]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    queue.append(adj)

        if len(res) < len(hashmap):
            return ""
        return res

sol = Solution()
words = ["wrt","wrf","er","ett","rftt"]
print(sol.alienOrder(words))
