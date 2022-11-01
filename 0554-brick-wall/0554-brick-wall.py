class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dic = {}
        MAX = 0
        for row in wall:
            endpoint = 0
            for i in range(len(row) - 1):
                endpoint += row[i]
                
                if endpoint in dic:
                    dic[endpoint] += 1
                else:
                    dic[endpoint] = 1
            
        c = dic.values()
        return len(wall) - (max(c) if c else 0)