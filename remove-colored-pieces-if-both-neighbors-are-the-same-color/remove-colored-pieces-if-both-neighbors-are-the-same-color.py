class Solution:
    def winnerOfGame(self, colors: str) -> bool:
    
        colors = list(colors)
        ali = 0
        bob = 0
        for i in range(len(colors)-2):
            if colors[i]==colors[i+1] and colors[i+1]==colors[i+2]:
                if colors[i] == "A" : ali += 1
                else: bob += 1
            
        
        return ali > bob
                    
                