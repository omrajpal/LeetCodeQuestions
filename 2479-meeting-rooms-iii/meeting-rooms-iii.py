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
        next_open = [] # (next meeting end time, room no)
        num_meetings = [0] * n
        free_rooms = list(range(n))
        meetings.sort() # might not be needed
        for s, e in meetings:
            while next_open and next_open[0][0] <= s:
                _, i = heapq.heappop(next_open)
                heapq.heappush(free_rooms, i)
            if free_rooms:
                room_no = heapq.heappop(free_rooms)
                prev_end = s
            else:
                prev_end, room_no = heapq.heappop(next_open)
            num_meetings[room_no] += 1
            if prev_end < s:
                prev_end = s
            heapq.heappush(next_open, (prev_end + (e - s), room_no))
            print((prev_end + (e - s), room_no))
            print(free_rooms)

        print(num_meetings)
        maxCount = 0
        max_room = 0
        for i, count in enumerate(num_meetings):
            if count > maxCount:
                max_room = i
                maxCount = count
        return max_room
        