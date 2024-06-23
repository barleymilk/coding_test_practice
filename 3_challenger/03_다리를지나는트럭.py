# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    complete = []

    qu_truck = deque(truck_weights)
    loading = deque()
    loading_time = deque()

    while True:
        time += 1

        # 담긴 시간과 현재 시간 빼서 끝내기 (out of range를 방지하기 위한 조건문 추가)
        if loading and time-loading_time[0] == bridge_length:
            complete.append(loading.popleft())
            loading_time.popleft()

            # 다 건넌 트럭 목록이 제시된 트럭 목록과 같으면 끝내기
            if complete == truck_weights:
                return time

        # 남은 대기 트럭이 1 이상이고, 무게 합이 weight를 넘지 않을 때 다리 건너기
        if len(qu_truck) >= 1 and sum(loading) + qu_truck[0] <= weight :
            loading.append(qu_truck.popleft())
            loading_time.append(time)
        
        print(f"qu_truck : {qu_truck}")
        print(f"loading : {loading}")
        print(f"loading_time : {loading_time}")
        print("=====================")

print(solution(2, 10, [7,4,5,6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
# print(solution(10, 20, [10, 10, 10]))