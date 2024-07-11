Here's the full description of the [problem](https://neetcode.io/problems/anagram-groups)

To solve this problem, we need to use a `hashmap` (dictionary) effectively.

A good method to determine if two strings are anagrams is to sort them and check if the sorted strings match.

We can follow these steps:

- Iterate through the elements of the array `strs`.
- For each element in `strs`, check if its sorted string is present in the `hashmap`.
- If it is, we have found the corresponding anagram, so we add the word to the list in the `hashmap` that has the sorted string as the key.
- If the sorted string is not present in the `hashmap`, we create a new list.
- Finally, we return the values of the `hashmap`.

Complexity:

The time complexity of this approach is `O(N⋅KlogK)`, where `N` is the number of strings and `K` is the maximum length of a string. This is because we sort each string, which takes `O(KlogK)`, and we do this for each of the 'N' strings.

Here is the complete solution:

```python 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str not in hashmap: 
                hashmap[sorted_str] = []
            hashmap[sorted_str].append(string)
            
        return list(hashmap.values())
```
This code correctly groups anagrams together by using the sorted version of each string as a key in a dictionary.