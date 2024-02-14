from typing import DefaultDict, List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = DefaultDict(int)
        players = set()

        for winner, loser in matches:
            losses[loser] += 1
            players.add(winner)
            players.add(loser)

        no_loss , one_loss = [], []

        for player in players:
            if not losses[player]:
                no_loss.append(player)
            elif losses[player] == 1:
                one_loss.append(player)
        
        return [sorted(no_loss), sorted(one_loss)]