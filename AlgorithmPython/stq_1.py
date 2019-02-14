#deque를 스택처럼 이용하여 푼 풀이.


def solution(arrangement):
    from collections import deque
    answer = 0
    dq = deque()
    before = None
    for i in arrangement:
        if i == '(':
            dq.append('(')
        else:
            if before == '(':
                before = dq.pop()
                answer += len(dq)
            if before == ')':
                dq.pop()
                answer += 1
        before = i
    return answer


st = "()(((()())(())()))(())"
print(solution(st))

