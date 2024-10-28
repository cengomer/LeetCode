import heapq
from collections import defaultdict

class Twitter(object):

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)   # Maps userId to list of (count, tweetId)
        self.followMap = defaultdict(set)   # Maps userId to set of followeeIds

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1  # Decrement to simulate timestamp (more recent tweets have smaller counts)

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        :type userId: int
        :rtype: List[int]
        """
        res = []
        minHeap = []

        # Ensure the user follows themselves
        self.followMap[userId].add(userId)

        # Collect the most recent tweet from each followee
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap and self.tweetMap[followeeId]:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, (count, tweetId, followeeId, index - 1))

        # Extract up to 10 most recent tweets
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                next_count, next_tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, (next_count, next_tweetId, followeeId, index - 1))

        return res

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
