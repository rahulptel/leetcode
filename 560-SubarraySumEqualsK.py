class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize the hashmap to store prefix sum and the number of 
        # indices with that prefix sum
        hashmap = {0: 1}

        # Initialize counters
        n_subarrays = 0
        prefixSum = 0

        # For each index j, check if prefix_sum_j - k is in hashmap
        for i, num in enumerate(nums):
            prefixSum += num
            
            # Subarray found if prefix present in hashmap
            query = prefixSum - k                
            if query in hashmap:
                n_subarrays += hashmap[query]
            
            if prefixSum not in hashmap:
                hashmap[prefixSum] = 1
            else:
                hashmap[prefixSum] += 1

        return n_subarrays



        
