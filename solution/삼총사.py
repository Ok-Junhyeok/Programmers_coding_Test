def solution(number):
    answer = 0

    for i in range(len(number)):
        for j in range(1, len(number)):
            for k in range(2, len(number)):
                if i >= j or i >= k or j >= k:
                    continue
                result = number[i] + number[j] + number[k]

                if result == 0:
                    answer += 1
    return answer


print(solution([-2, 3, 0, 2, -5]))
print(solution([-3, -2, -1, 0, 1, 2, 3]))
print(solution([-1, 1, -1, 1]))
