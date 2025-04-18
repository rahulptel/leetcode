class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pairWeights = [weights[i] + weights[i+1] for i in range(n-1)]
        pairWeights.sort()
        return sum(pairWeights[::-1][:k-1]) - sum(pairWeights[:k-1])
