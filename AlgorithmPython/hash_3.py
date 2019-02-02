# dict를 이용한 코드
def solution( clothes ):
    answer = 1
    dict = {}

    for i in clothes:
        if i[1] in dict.keys():
            dict[i[1]].append(i[0])
        else:
            dict[i[1]] = [i[0]]

    for i in dict.keys():
        answer *= len(dict[i])+1

    return answer-1


clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
print(solution(clothes))
'''
collections의 Counter와 functools의 reduce를 사용한 풀이. 내 코드는 파이써닉하지 않은 코드이고 이 코드가 더 파이써닉하다.
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
'''