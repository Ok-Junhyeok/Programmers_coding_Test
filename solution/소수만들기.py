def solution(nums):
    answer = -1

    #1,2,3
    #1,2,4
    #2,3,4

    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                sum = 0
                if isEqualorBigger(i, j, k):
                    continue
                sum += nums[i]+nums[j]+nums[k]
                primary = isPrimary(sum)
                if primary != 0:
                    answer += 1

    if answer == -1:
        return answer
    return answer+1

def isEqualorBigger(i, j, k):
    return i >= j or i >= k or j >= k

def isPrimary(num):
    flag = 0
    for i in range(2, num):
        if num % i == 0:
            return flag
    return num


print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))