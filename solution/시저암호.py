def solution(s, n):
    trans_list = list(s)

    for i in range(len(trans_list)):
        if trans_list[i] == " ":
            continue
        trans_list[i] = chr(transfer_Z2A(trans_list[i], n))

    answer = ''.join(trans_list)
    return answer

def transfer_Z2A(word, n):
    num = ord(word) + n
    if word.islower():
        if num > ord('z'):
            num -= 26
        return num
    if word.isupper():
        if num > ord('Z'):
            num -= 26
        return num

print(solution('AB', 1))
print(solution('z', 1))
print(solution('Z', 1))
print(solution('a B z', 4))
print(solution('a', 1))
print(solution('a       z    x              B ', 25))