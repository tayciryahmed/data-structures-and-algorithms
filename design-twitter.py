from time import time 

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follower_followees = collections.defaultdict(list) # follower: [followees]
        self.tweets = collections.defaultdict(list) # user: [posts]
                

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId] += [(tweetId, time())]
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        candidates = []
        for x in set(self.follower_followees[userId]+[userId]):
            candidates += self.tweets[x] 
        
        candidates.sort(key=lambda x: x[1], reverse=True)
        
        return [x[0] for x in candidates[:10]]
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follower_followees[followerId] += [followeeId]
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.follower_followees[followerId]:
            self.follower_followees[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
