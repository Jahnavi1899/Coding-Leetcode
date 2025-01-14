class Solution:
    def minimumCardPickup(self, cards) -> int:
        l, r = 0, 0
        n = len(cards)
        cardsmap = {}
        res = float('inf')

        while r < n:
            if cards[r] in cardsmap:
                cardsmap[cards[r]] += 1
            else:
                cardsmap[cards[r]] = 1

            while cardsmap[cards[r]] == 2:
                if cards[l] == cards[r]:
                    res = min(res, r-l+1)
                cardsmap[cards[l]] -= 1
                l += 1
            r += 1
        if res == float('inf'):
            return -1
        return res
        
cards = [3,4,2,3,4,7]
obj = Solution()
print(obj.minimumCardPickup(cards))