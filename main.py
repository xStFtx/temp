class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # Sort the balloons by their end point
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        end = points[0][1]  # end point of the first balloon
        
        for i in range(1, len(points)):
            if points[i][0] > end:  # if the next balloon starts after the end point
                arrows += 1
                end = points[i][1]  # update the end point
        return arrows