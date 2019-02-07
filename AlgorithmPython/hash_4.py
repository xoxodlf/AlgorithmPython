import collections
from collections import Counter
def solution(genres, plays):
    answer = []
    dict={}
    dictCnt = {}
    for i in range(len(genres)):
        if genres[i] in dict.keys():
            dict[genres[i]].append((plays[i], i))
            dictCnt[genres[i]] += plays[i]
        else:
            dict[genres[i]] = [(plays[i], i)]
            dictCnt[genres[i]] = plays[i]

    dictCnt = sorted(dictCnt, key=lambda k: dictCnt[k], reverse=True)

    for i in dictCnt:
        tmp = sorted(dict[i], key= lambda k: (k[0], -k[1]), reverse=True)
        index = 0
        for j in tmp:
            answer.append(j[1])
            index += 1
            if index == 2:
                break
    return answer


genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))

'''
파이써닉한코드
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer
'''