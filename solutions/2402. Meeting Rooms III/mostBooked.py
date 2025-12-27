"""
You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during
the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
1. If there are no available rooms, the meeting will be delayed until a room becomes free.
The delayed meeting should have the same duration as the original meeting.
2. When a room becomes unused, meetings that have an earlier original start time should be given the room.
3. Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.
"""

from typing import List
import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        busy_rooms = []
        room_meeting_count = [0] * n

        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                free_time, room_number = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room_number)

            if free_rooms:
                room_number = heapq.heappop(free_rooms)
                actual_start = start
            else:
                free_time, room_number = heapq.heappop(busy_rooms)
                actual_start = free_time

            actual_end = actual_start + (end - start)
            heapq.heappush(busy_rooms, (actual_end, room_number))
            room_meeting_count[room_number] += 1

        max_meetings = max(room_meeting_count)
        for i in range(n):
            if room_meeting_count[i] == max_meetings:
                return i


# Test cases:
if __name__ == "__main__":
    solution = Solution()

    n1 = 2
    meetings1 = [[0, 10], [1, 5], [2, 7], [3, 4]]
    print(solution.mostBooked(n1, meetings1))  # Output: 0

    n2 = 3
    meetings2 = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
    print(solution.mostBooked(n2, meetings2))  # Output: 1
