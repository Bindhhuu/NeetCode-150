class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followees = defaultdict(set)
        self._time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.followees:
            self.followees[userId]
        self.tweets[userId].append((self._time, tweetId))
        self._time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        # gather the set of sources: the user plus everyone they follow
        sources = set(self.followees.get(userId, set()))
        sources.add(userId)

        heap = []
        for uid in sources:
            user_tweets = self.tweets.get(uid)
            if user_tweets:
                idx = len(user_tweets) - 1
                time, tid = user_tweets[idx]
                # push (-time, tweetId, uid, idx)
                heapq.heappush(heap, (-time, tid, uid, idx))

        while heap and len(res) < 10:
            neg_time, tid, uid, idx = heapq.heappop(heap)
            res.append(tid)
            if idx - 1 >= 0:
                prev_time, prev_tid = self.tweets[uid][idx - 1]
                heapq.heappush(heap, (-prev_time, prev_tid, uid, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return  # no-op, following self isn't needed
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees.get(followerId, set()):
            self.followees[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
