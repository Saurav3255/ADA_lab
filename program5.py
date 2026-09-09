from typing import List
from dataclasses import dataclass


# -------------------------------
# 1. Fractional Knapsack
# -------------------------------
def fractional_knapsack(weights: List[int], values: List[int], capacity: int) -> float:
    """
    Returns the maximum attainable profit using Fractional Knapsack.
    """

    # Create (value/weight ratio, weight, value)
    items = []

    for weight, value in zip(weights, values):
        ratio = value / weight
        items.append((ratio, weight, value))

    # Sort by value/weight ratio in descending order
    items.sort(reverse=True)

    total_profit = 0.0
    remaining_capacity = capacity

    for ratio, weight, value in items:

        if remaining_capacity == 0:
            break

        # Take complete item
        if weight <= remaining_capacity:
            total_profit += value
            remaining_capacity -= weight

        # Take fraction of item
        else:
            fraction = remaining_capacity / weight
            total_profit += value * fraction
            remaining_capacity = 0

    return total_profit


# -------------------------------
# 2. Job Scheduling with Deadlines
# -------------------------------
@dataclass
class Job:
    job_id: int
    deadline: int
    profit: int


def job_scheduling(jobs: List[Job]) -> List[int]:
    """
    Returns the optimal sequence of job IDs that maximizes profit.
    Each job takes one unit of time.
    """

    # Sort jobs according to decreasing profit
    jobs.sort(key=lambda job: job.profit, reverse=True)

    # Find maximum deadline
    max_deadline = max(job.deadline for job in jobs)

    # Time slots
    slots = [None] * (max_deadline + 1)

    # Schedule jobs
    for job in jobs:

        # Find the latest available slot before deadline
        for t in range(job.deadline, 0, -1):

            if slots[t] is None:
                slots[t] = job.job_id
                break

    # Return scheduled job IDs
    return [job_id for job_id in slots[1:] if job_id is not None]


# -------------------------------
# Main Program
# -------------------------------
if __name__ == "__main__":

    # Fractional Knapsack Example
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    profit = fractional_knapsack(weights, values, capacity)

    print("Fractional Knapsack")
    print("Maximum Profit:", profit)


    # Job Scheduling Example
    jobs = [
        Job(1, 2, 100),
        Job(2, 1, 19),
        Job(3, 2, 27),
        Job(4, 1, 25),
        Job(5, 3, 15)
    ]

    sequence = job_scheduling(jobs)

    print("\nJob Scheduling")
    print("Optimal Job Sequence:", sequence)
