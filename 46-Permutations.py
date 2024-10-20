class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []

        def create_perms(p, opts):
            if len(opts) == 0:
                perms.append(p)
                return

            for i, o in enumerate(opts):
                p_ = p[:]
                p_.append(o)
                opts.pop(i)
                create_perms(p_, opts)
                opts.insert(i, o)

        create_perms([], nums)
        return perms
        
