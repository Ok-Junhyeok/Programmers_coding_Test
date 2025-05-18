def solution(n):
    answer = 0
    for i, val in enumerate(deci_3(n)):
        sum_element = val * (3**i)
        answer += sum_element
    return answer

def deci_3(n):
    deciList = []
    while True:
        # if 조건문이 거짓이면, mod의 수를 리스트에 추가
        # if 조건문이 참이 되면, n을 리스트에 추가 후 리스트 뒤집기

        if n <= 2:
            deciList.append(n)
            break

        mod = n % 3
        n = n // 3
        deciList.append(mod)

    return deciList[::-1]

print(solution(45))
#45 / 3 = 15-0
#15 / 3 = 5-0
#5 / 3 = 1-2
# 1 / 3 = 0-1
print(solution(125))