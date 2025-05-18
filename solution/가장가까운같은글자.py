def solution(s):
    answer = []

    for i in range(len(s)):
        equal_val = -10
        for j in range(i, -1, -1):
            if s[j] == s[i]:
                if i == j:
                    continue
                else:
                    equal_val = j
                    break

        if equal_val == -10:
            answer.append(-1)
        else:
            answer.append(i - equal_val)

    return answer

# 실패 케이스
print(solution("vvvvvvvvvvvv"))


# 성공 케이스
# print(solution("banana"))
# print(solution("foobar"))