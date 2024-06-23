# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_dict = {"(": ")", "{": "}", "[": "]"}
        valid_queue = []
        for parenthesis in s:
            # 왼쪽 괄호일 때 -> 추가
            if parenthesis in parenthesis_dict.keys():
                valid_queue.append(parenthesis)
            # 오른쪽 괄호일 때
            else: 
                if valid_queue == []:
                    return False
                else:
                    top = valid_queue.pop()
                    if parenthesis_dict[top] != parenthesis:
                        return False
        if len(valid_queue) > 0:
            return False
        
        return True
    
solution = Solution()
print(solution.isValid("[]"))