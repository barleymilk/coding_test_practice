# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville and scoville[0] < K:
        try:
            food1 = heapq.heappop(scoville)
            food2 = heapq.heappop(scoville)
            heapq.heappush(scoville, food1 + (food2 * 2))
            answer += 1
        except:
            return -1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7)) # 2