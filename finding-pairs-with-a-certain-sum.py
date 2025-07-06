from typing import Counter, List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)
        

    def add(self, index: int, val: int) -> None:
        old = self.nums2[index]
        self.freq[old] -= 1

        if self.freq[old] == 0:
            del self.freq[old]

        self.nums2[index] += val
        new_val = self.nums2[index]
        self.freq[new_val] += 1
        

    def count(self, tot: int) -> int:
        count = 0
        for i in self.nums1:
            if tot - i in self.freq:
                count += self.freq[tot - i]
             

        return count
        

fsp = FindSumPairs([1,1,2,2,2,3],[1,4,5,2,5,4])
print(fsp.add(3,2))