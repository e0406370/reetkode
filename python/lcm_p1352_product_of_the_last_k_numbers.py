"""
LCM 1352. Product of the Last K Numbers

Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

Implement the ProductOfNumbers class:
- ProductOfNumbers() Initializes the object with an empty stream.
- void add(int num) Appends the integer num to the stream.
- int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.

The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

Constraints:
- 0 <= num <= 100
- 1 <= k <= 4 * 10^4
- At most 4 * 10^4 calls will be made to add and getProduct.
- The product of the stream at any point in time will fit in a 32-bit integer.

Topics:
- Array
- Math
- Design
- Data Stream
- Prefix Sum
"""


class ProductOfNumbers:
    # O(1)
    def __init__(self):
        self.nums = []
        self.prefix_products = []

    # O(1)
    def add(self, num: int) -> None:
        self.nums.append(num)

        if num == 0:
            self.prefix_products = []

        elif not self.prefix_products:
            self.prefix_products.append(num)

        else:
            self.prefix_products.append(num * self.prefix_products[-1])

    # O(1)
    def getProduct(self, k: int) -> int:
        size = len(self.prefix_products)

        if k > size:
            return 0

        elif k == size:
            return self.prefix_products[-1]

        else:
            return self.prefix_products[-1] // self.prefix_products[size - k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)


# Time Complexity: O(1) - 27 ms -> 86.30%
# Space Complexity: O(n) - 32.12 MB -> 13.55%
