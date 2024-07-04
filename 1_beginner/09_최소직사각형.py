# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    min_list = []
    max_list = []
    for size in sizes:
        min_list.append(min(size))
        max_list.append(max(size))
    return max(min_list) * max(max_list)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]])) # 4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])) # 120
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])) # 133