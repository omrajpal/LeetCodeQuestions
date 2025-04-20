import bisect

class Twitter(object):

    def __init__(self):
        self.feed = [] ## [(userId, tweetId), ...]
        self.users = {} ## {userId: set(following), ...}

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if userId not in self.users.keys():
            self.users[userId] = set()
        self.feed.append((userId, tweetId))
        
        
    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.users.keys():
            return []
        self.users[userId].add(userId)
        following = self.users[userId]
        return [i for u, i in self.feed if u in following][-10:][::-1]
        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.users.keys():
            self.users[followerId] = set()
        self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)