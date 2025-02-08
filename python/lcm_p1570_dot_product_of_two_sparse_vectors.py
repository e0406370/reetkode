"""
  LCM 1570. Dot Product of Two Sparse Vectors (Premium)

  Given two sparse vectors, compute their dot product.

  Implement class SparseVector:
  - SparseVector(nums) Initializes the object with the vector nums
  - dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
  
  A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

  Constraints:
  - n == nums1.length == nums2.length
  - 1 <= nums[i] <= 10^5
  - 0 <= nums1[i], nums2[i] <= 100

  Topics:
  - Array 
  - Hash Table 
  - Two Pointers
  - Design
"""


# Time Complexity: O(n) - 1305 ms -> 90.05%
# Space Complexity: O(n) - 21.70 MB -> 66.84%
class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.vector[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        res = 0
        for i in self.vector.keys():
            if i in vec.vector:
                res += self.vector[i] * vec.vector[i]

        return res


# Time Complexity: O(n) - 1338 ms -> 44.10%
# Space Complexity: O(n) - 21.90 MB -> 46.74%
class SparseVectorAlt:
    def __init__(self, nums: List[int]):
        self.vector = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVectorAlt") -> int:
        return sum([a * b for a, b in zip(self.vector, vec.vector)])


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

"""
  methods:
  1. hash map to store non-zero values and their corresponding indices
  2. non-efficient array approach of storing all nums
"""
