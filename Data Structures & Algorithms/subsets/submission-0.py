class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #at every level we can either choose to add into 
        #our result array or choose not to

        res = []
        subset = []   #[1,2,3]

        def backtrack(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
            backtrack(i+1)


        backtrack(0)

        return res
