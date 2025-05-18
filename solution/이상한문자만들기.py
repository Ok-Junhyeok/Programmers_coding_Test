def solution(s):
    answer = ''
    s_split = s.split(" ")

    for a in s_split:
        for i, val in enumerate(a):
            if i % 2 == 0:
                answer += val.upper()
            else:
                answer += val.lower()
        answer += " "
    return answer[0:-1]


print(solution("try hello world"))
