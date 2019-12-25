class Solution:
    # DFS
    def permute(self, nums):
        res, origLen = [], len(nums)

        def dfs(count, avail, newPerm):
            if count == origLen:
                return res.append(newPerm)
            for i in range(len(avail)):
                dfs(count+1, avail[:i] + avail[i+1:], newPerm + [avail[i]])

        dfs(0, nums, [])
        return res


s = Solution()
print(s.permute([1, 2, 3]))
