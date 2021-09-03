
def solution(nums, target):
    map = {}
    for idx, num in enumerate(nums):
        if num in map:
            return idx, map[num]
        else:
            map[target - num] = idx

"""https://leetcode.com/problems/two-sum/"""