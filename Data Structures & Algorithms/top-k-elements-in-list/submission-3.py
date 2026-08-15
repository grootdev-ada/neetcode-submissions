class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       counts = {}
       for num in nums :
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
       sorted_dict = sorted(counts.items(), key=lambda item: item[1], reverse=True)
       result = []
       for i in range(k):
        result.append(sorted_dict[i][0])
       return result