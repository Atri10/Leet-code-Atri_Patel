class Solution:
    def merge(self, Intervals: List[List[int]]) -> List[List[int]]:
        
            Intervals.sort()

            stack = []
            stack.append(Intervals[0])

            for Int in Intervals[1:]:

                L = Int[0]
                R = Int[1]

                if stack[-1][0] <= L <= stack[-1][1]:
                    stack[-1][1] = max(stack[-1][1],R)

                else:
                    stack.append(Int)

            return stack