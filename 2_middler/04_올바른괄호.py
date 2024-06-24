# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = 0
    for p in s:
        if stack == 0 and p == ")":
            return False
        elif stack > 0 and p == ")":
            stack -= 1
        if p == "(":
            stack += 1
    if stack == 0:
        return True
    return False

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))