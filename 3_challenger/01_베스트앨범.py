# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    play_dict = {}
    for i, genre in enumerate(genres):
        if genre in play_dict:
            play_dict[genre][0] += plays[i]
        else:
            play_dict[genre] = [plays[i]]
        play_dict[genre] += [(i, plays[i])]
    
    # 플레이 수를 기준으로 장르 내림차순 정렬
    play_dict = dict(sorted(play_dict.items(), key=lambda x: x[1][0], reverse=True))

    # 장르별로 플레이수 많은 순으로 2곡 이하 뽑기
    answer = []
    for p in play_dict:
        temp = play_dict[p][1:]
        temp = list(sorted(temp, key=lambda x: x[1], reverse=True))
        answer += [temp[0][0]]
        if len(temp) > 1:
            answer += [temp[1][0]]

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))