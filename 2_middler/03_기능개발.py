# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    result = []
    compare_point = 0

    for a, b, in zip(progresses, speeds):
        working_time = (100 - a) // b + 1 if (100 - a) % b else (100 - a) // b

        if len(result) == 0:
            result.append(1)
            compare_point = working_time
        else:
            if working_time > compare_point:
                result.append(1)
                compare_point = working_time
            else:
                result[-1] += 1
    
    return result

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))