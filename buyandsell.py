def maxProfit(prices):
        # brute force approach
        n = len(prices)
        min_price = min(prices)
        idx1 = prices.index(min_price)
        if idx1 == n-1:
                return 0
        else:
            subarr = prices[idx1+1:]
            max_price = max(subarr)
            if max_price > min_price:
                return max_price - min_price
            return 0

prices = [7,6,4,3,1]
print(maxProfit(prices))