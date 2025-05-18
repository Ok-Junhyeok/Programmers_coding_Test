def solution(number, limit, power):
    answer = 0
    steel = []
    for i in range(1, number + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
            if count >= limit:
                break
        answer += count
        # steel.append(over_power(count, limit, power))
    # answer = sum(steel)
    return answer

def over_power(count, limit, power):
    if count > limit:
        return power
    return count


print(solution(5, 3, 2))
print(solution(10, 3, 2))