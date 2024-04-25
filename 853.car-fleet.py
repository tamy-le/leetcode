#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#


# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        reach_times_by_pos = list(
            map(
                lambda x: (target - x[0]) / x[1],
                sorted(zip(position, speed), reverse=True),
            )
        )
        result = [reach_times_by_pos[0]]
        for reach_time in reach_times_by_pos[1:]:
            if reach_time > result[-1]:
                result.append(reach_time)
        return len(result)


# @lc code=end
# Time: O(nlogn) -> sort
# Memory: O(n) -> don't count result
