class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        rows, cols = len(image), len(image[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]] #bottom, top, right, left

        start = image[sr][sc]
        image[sr][sc] = color
        queue = [[sr, sc]]
        # visited = set()

        while queue:
            top_r, top_c = queue.pop(0)
            for r, c in directions:
                dr, dc = top_r + r, top_c + c
                if (
                    dr in range(rows) and
                    dc in range(cols) and
                    image[dr][dc] == start
                ):
                    if image[dr][dc] == color:
                        continue
                    else:
                        image[dr][dc] = color

                        queue.append([dr, dc])

        return image
    

image = [[0,0,0],[0,0,0]]
sr, sc = 0, 0
color = 0

obj = Solution()
print(obj.floodFill(image, sr, sc, color))

