# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    hash = {}
    for p in participant:
        if p in hash:
            hash[p] += 1
        else:
            hash[p] = 1
    for c in completion:
        if hash[c] == 1:
            del hash[c]
        else:
            hash[c] -= 1

    return list(hash.keys())[0]
    # for c in completion:
    #     participant.remove(c)
    # return participant[0]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"])) # leo
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])) # vinko
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])) # mislav