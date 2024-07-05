# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    test = [0, 0, 0]
    supoja1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    supoja2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    supoja3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i, answer in enumerate(answers):
        if supoja1[i % 10] == answer:
            test[0] += 1
        if supoja2[i % 16] == answer:
            test[1] += 1
        if supoja3[i % 20] == answer:
            test[2] += 1
    
    result = []
    for i, t in enumerate(test):
        if t == max(test):
            result.append(i + 1)

    return result

print(solution([1,2,3,4,5])) # [1]
print(solution([1,3,2,4,2])) # [1,2,3]