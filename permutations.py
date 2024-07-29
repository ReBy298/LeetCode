class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursive(n, res=[], perms=[]):
            if not n:
                res.append(perms[:])
                return
            for i in range(len(n)):
                perms.append(n[i])
                recursive(n[:i] + n[i+1:], res, perms)
                perms.pop()
        
        result = []
        recursive(nums, result)
        return result