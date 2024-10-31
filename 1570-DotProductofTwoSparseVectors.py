class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = {i: n for i, n in enumerate(nums) if n != 0}
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        x, y = (self.d, vec.d) if len(self.d) < len(vec.d) else (vec.d, self.d)
            
        result = 0
        for xi, xv in x.items():
            if xi in y:
                result += xv * y[xi]
            
        return result
            

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
