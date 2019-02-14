# 코드를 짰는데 너무 마음에 안든다 더 심플한 방법이 있을 것이다.


def solution(priorities, location):
    import collections
    answer = 0
    kcnt = 0
    cnt = collections.Counter(priorities)
    kvals = sorted(cnt, key=lambda k: k, reverse=True)
    now = kvals[kcnt]
    i = 0
    while(True):
        if priorities[i%len(priorities)] == now:
            if location == i%len(priorities):
                break
            cnt[now] -= 1
            answer += 1
            if cnt[now] == 0:
                kcnt += 1
                now = kvals[kcnt]
        i += 1
    return answer+1


arr = [2, 1, 3, 2]
loc = 2
print(solution(arr, loc))
'''

def solution(p, l):
    ans = 0
    m = max(p)
    while True:
        v = p.pop(0)
        if m == v:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return ans


'''