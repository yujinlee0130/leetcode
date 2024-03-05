class Solution_217:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mymap = defaultdict(int)
        for num in nums:
            if mymap[num] > 0:
                return True
            mymap[num] += 1
        return False