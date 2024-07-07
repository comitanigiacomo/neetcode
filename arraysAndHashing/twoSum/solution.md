Here's the full description of the [problem](https://neetcode.io/problems/two-integer-sum)

The problem can be tackled initially with a straightforward brute force approach:

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target: return [i,j]
        return # Non servirebbe dato che ho la certezza che la coppia esista sempre
```

This brute force solution has a time complexity of O(n^2) which can be improved. A more efficient approach uses a hash map (dictionary) to reduce the time complexity to O(n): 

1. Iterate through the array `nums`.
2. For each element, calculate the difference `diff` between the target and the current element.
3. Check if `diff` is already in the hash map.
4. If `diff` is found, return the indices of the current element and the element corresponding to diff.
5. If `diff` is not found, add the current element and its index to the hash map.
6. Continue the iteration until the solution is found.

This approach leverages the hash map to achieve an average time complexity of O(n) with a space complexity of O(n).

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums): 
            diff = target - n 
            if diff in hashmap: 
                return [hashmap[diff], i]
            hashmap[n] = i 
        return 
```

This solution is more efficient because it reduces the number of operations needed to find the pair of indices that sum to the target. By using a hash map, we store the necessary information to find the solution in constant time for each element.