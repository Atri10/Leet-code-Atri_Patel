class Solution:
    def addBinary(self, a: str, b: str) -> str: return (bin(int(str(a),2) + int(str(b),2)))[2:]