# https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3
def solution(nums):
    max_num = len(set(nums))
    return min(len(nums)//2, max_num)

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))