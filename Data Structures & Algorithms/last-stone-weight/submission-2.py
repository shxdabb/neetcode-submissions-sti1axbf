import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] #stones = [-2,-7,-4,-1,-8,-1]
        
        heapq.heapify(stones) #stones = [-8,-7,-4,-2,-1,-1]

        while len(stones)>1:
            max1 = abs(heapq.heappop(stones)) #8
            max2 = abs(heapq.heappop(stones)) #7

            if max1 > max2:
                heapq.heappush(stones,-(max1-max2))
            
        return abs(stones[0]) if stones else 0
