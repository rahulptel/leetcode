class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 1

        start_times = [s for s, _ in intervals]
        end_times = [e for _, e in intervals]        
        
        start_times.sort()
        end_times.sort()

        max_rooms, n_rooms = 0, 0
        i, j = 0, 0
        while i < len(start_times):
            # Starting a job
            if start_times[i] < end_times[j]:
                n_rooms += 1
                if max_rooms < n_rooms:
                    max_rooms = n_rooms

                i += 1
            # Finishing a job
            elif start_times[i] > end_times[j]:
                n_rooms -= 1
                j += 1
            # Start and finish time same. 
            # Complete the job before starting the new one
            else:
                i += 1
                j += 1

        return max_rooms




