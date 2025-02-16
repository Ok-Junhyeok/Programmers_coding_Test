def solution(arr):
    unique_list = list(set(arr))
    unique_list.sort(reverse=True)
    return unique_list

arr = [1, 1, 3, 3, 2,4,10, 6, -1, 3]
print(solution(arr))


