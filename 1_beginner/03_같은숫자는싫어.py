# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    for a in arr:
        if len(answer) == 0 or answer[-1] != a:
            answer.append(a)
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))

