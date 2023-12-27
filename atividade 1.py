def solution(nums: list[int], target: int) -> list[int]:
        for i, e in enumerate(nums):
                for j, k in enumerate(nums):
                        if i == j:
                                continue
                        if e + k == target:
                                return [i, j]