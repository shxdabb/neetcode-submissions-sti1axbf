class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #at every level we can either choose to add into 
        #our result array or choose not to

        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            # res.append(subset[:])
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res


 