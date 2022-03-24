class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        l = 0
        h = len(people) - 1
        b = 0
        people.sort()
        
        while l <= h:
            
            if people[l] + people[h] <= limit:
                l += 1
                h -= 1
            else:
                h -= 1
            
            b += 1
                
        return b