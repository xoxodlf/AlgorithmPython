# 딕셔너리를 이용한 코드
phone_book = ['119', '97674223', '1195524421']


def solution(phone_book):
    answer = True
    dict = {}
    for i in phone_book:
        for j in dict.keys():
            if len(i)< len(j):
                if i == j[:len(i)]:
                    return False
            else:
                if j == i[:len(j)]:
                    return False
        dict[i]=1

    return answer


print(solution(phone_book))

'''
sort해서 순서대로 정렬 후, 현재 인덱스와 다음 인덱스를 비교
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
'''