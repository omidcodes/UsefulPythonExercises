class RecentCounter(object):


    def __init__(self):

        self.requests = []
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.requests.append(t)

        number_of_request_in_the_last_3000_seconds = 0

        for i in range(len(self.requests) -1 , -1, -1):
            
            if t - 3000 <= self.requests[i] <= t:
                number_of_request_in_the_last_3000_seconds += 1 
            else: 
                break

        return number_of_request_in_the_last_3000_seconds




# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

recentCounter = RecentCounter()
recentCounter.ping(1);     # // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   # // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  # // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  # // requests = [1, 100, 3001, 3002], range is [2,3002], return 3