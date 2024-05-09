# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 10^5
# -104 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

def top_k_frequent(nums, k):
    freq = {}
    for num in nums:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1
    return [num for num, _ in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]]