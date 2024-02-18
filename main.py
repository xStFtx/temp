class Solution:

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meetings.sort() # make sure start times are sorted!!

        

        meetingCount = [0 for _ in range(n)]

        availableRooms = list(range(n)); heapify(availableRooms)

        occupiedRooms = []

        

        

        for start, end in meetings:

            while occupiedRooms and start >= occupiedRooms[0][0]:

                heappush(availableRooms, heappop(occupiedRooms)[1]) # frees room and makes it available

            

            if availableRooms:

                roomNumber = heappop(availableRooms)  # assigns next available room

            else:

                freedEnd, roomNumber = heappop(occupiedRooms)  # waits until the next room that would be available gets free

                end += freedEnd - start

            heappush(occupiedRooms, (end,roomNumber))  # make note that the ruom is occupied and when the assigned meeting ends

            meetingCount[roomNumber] += 1  # update meeting counter

            

        return sorted([(count, i) for i, count in enumerate(meetingCount)], key = lambda x: (-x[0], x[1]))[0][1]  # find room with most meetings