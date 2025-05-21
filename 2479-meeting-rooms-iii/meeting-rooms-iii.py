class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        # hashmap for each room and count of meetings room_no -> count, 
        # waiting queue of meetings by start time, maybe not needed bc for look
        # array of next open meeting for each room?
        meetings.sort()
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        in_use = []  # min-heap of (end_time, room_no)
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free rooms that are now available
            while in_use and in_use[0][0] <= start:
                _, room = heapq.heappop(in_use)
                heapq.heappush(free_rooms, room)

            if free_rooms:
                room = heapq.heappop(free_rooms)
                new_end = start + duration
            else:
                earliest_end, room = heapq.heappop(in_use)
                new_end = earliest_end + duration

            count[room] += 1
            heapq.heappush(in_use, (new_end, room))

        # Final scan for max meeting count with tie-breaking
        return max(range(n), key=lambda i: (count[i], -i))