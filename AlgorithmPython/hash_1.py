participant = ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']

#딕셔너리를 이용한 코드
def solution(participant , completion):
    dict={}
    answer = ''
    for i in participant:
        if i in dict:
            dict[i] = dict.get(i)+1
        else:
            dict[i] = 1

    for i in completion:
        dict[i] = dict.get(i)-1

    for i in dict.keys():
        if dict.get(i) == 1:
            answer = i
            break

    return answer

print(solution(participant,completion))


"""
콜렉션을 이용해 짠 코드.
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

"""