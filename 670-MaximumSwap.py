class Solution:
    def maximumSwap(self, num: int) -> int:        
        if num < 10:
            return num

        num_list = []
        while num > 0:
            num_list.append(int(num % 10))
            num = num // 10
        
        candidate_found = False
        best_j = -1
        for i in range(0, len(num_list)):            
            pivot = num_list[len(num_list) - i - 1]
            max_digit = pivot

            for j in range(i+1, len(num_list)):                
                candidate = num_list[len(num_list) - j - 1]                
                if candidate != pivot and candidate >= max_digit:                    
                    candidate_found = True
                    best_j = j
                    max_digit = candidate

            if candidate_found:
                break

        if candidate_found:
            i_, j_ = len(num_list) - i - 1, len(num_list) - best_j - 1
            num_list[i_], num_list[j_] = num_list[j_], num_list[i_]

        total=0
        for i, num in enumerate(num_list):
            total += num * (10**i)
        
        return total
        
