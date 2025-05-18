def solution(players, callings):
    for i in range(len(callings)):
        index = players.index(callings[i])
        players[index], players[index - 1] = players[index - 1], players[index]

    return players

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

print(solution(players, callings))