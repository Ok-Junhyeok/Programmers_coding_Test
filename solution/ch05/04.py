def solution(answers):
    answer = []
    pattern = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    scores = [0] * 3
    for i in range(3):
        scores[i] = student_score(answers, pattern[i])

    max_score = max(scores)

    for i, score in enumerate(scores):
        if score == max_score:
            answer.append(i+1)
    return answer

def student_score(answers, pattern):
    score = 0
    for i in range(len(answers)):
        # 만약 answers[i]와 패턴과 일치한다면 score += 1
        # 6%5 = 1, 7%5 = 2, 8%5 = 3, ... , 23 % 10 = 3
        if answers[i] == pattern[i % len(pattern)]:
            score += 1
    return score

print(solution([1,2,3,4,5,1,2,3,4,5]))
