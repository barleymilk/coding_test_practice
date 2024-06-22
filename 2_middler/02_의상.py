# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    clothes_dict = {}
    for _, type in clothes:
        if type in clothes_dict:
            clothes_dict[type] += 1
        else:
            clothes_dict[type] = 1

    answer = 1
    for count in clothes_dict.values():
        answer *= (count + 1)  # 해당 종류의 아이템을 착용하지 않는 경우 포함

    return answer - 1  # 아무 아이템도 착용하지 않는 경우를 제외

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
print(solution([["a", "A"], ["b", "B"], ["c", "C"]]))