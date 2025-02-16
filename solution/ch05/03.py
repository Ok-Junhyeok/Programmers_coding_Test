def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
        ret = sorted(set(answer))
    return ret

numbers = [2, 1, 3, 4, 1]
print(solution(numbers))