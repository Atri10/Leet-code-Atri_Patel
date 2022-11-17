class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        area1 = abs(C-A)*abs(B-D)
        area2 = abs(E-G)*abs(F-H)
        w = min(C,G)-max(A,E)
        h = min(D, H)-max(B,F)
        if w<=0 or h<=0:
            return area1 + area2
        else:
            return area1 + area2 - w*h