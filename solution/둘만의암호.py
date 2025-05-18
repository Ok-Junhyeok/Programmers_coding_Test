def solution(s, skip, index):
    transferByS = transfer(s)
    transferBySkip = transfer(skip)

    for i in range(len(transferByS)):
        num = 1
        while num <= index:
            if transferByS[i] in transferBySkip:
                transferByS[i] += 1
                continue
            transferByS[i] += 1
            if transferByS[i] > ord("z"):
                transferByS[i] = ord("a")
            num += 1

    answer = str()
    for i in range(len(transferByS)):
        answer += chr(transferByS[i])
    return answer

def transfer(str):
    trans = []
    for i in range(len(str)):
        trans.append(ord(str[i]))
    return trans


print(solution("aukks", "wbqd", 5))