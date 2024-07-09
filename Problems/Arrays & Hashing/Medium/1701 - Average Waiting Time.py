from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        start_time = customers[0][0]
        wait_time = customers[0][1]
        end_time = start_time + wait_time

        for i in range(1, len(customers)):
            start_time = max(end_time, customers[i][0])
            end_time = start_time + customers[i][1]
            wait_time += end_time - customers[i][0]

        return wait_time / len(customers)