class Twitter:

    def __init__(self):
        self.userPosts = dict()
        self.userFollows = dict()
        self.allPosts = list()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.allPosts.append((userId, tweetId)) 

    def getNewsFeed(self, userId: int) -> List[int]:
        rslt = []
        for post in reversed(self.allPosts):
            if len(rslt) == 10:
                return rslt
            
            followers = self.userFollows.get(userId, set())

            if post[0] in followers or post[0] == userId:
                rslt.append(post[1])
        
        return rslt

    def follow(self, followerId: int, followeeId: int) -> None:
        followers = self.userFollows.get(followerId)

        if followers is None:
            followers = set()
        
        followers.add(followeeId)
        self.userFollows[followerId] = followers

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followers = self.userFollows.get(followerId)

        if followers is None:
            return

        followers.discard(followeeId)
        self.userFollows[followerId] = followers