import praw
import urllib.request
import sys
sys.path.append("../RedditVk/")
import DownloadingPics

class DownloadingReddit(DownloadingPics.DownloadingPics):
    def __init__(self):
        self.__reddit = None
        self.__subreddit = None
    
    def initReddit(self, client_id, client_secret, password, username, user_agent):
        self.__reddit = praw.Reddit(client_id=client_id,
                    client_secret=client_secret,
                    password=password,
                    username=username,
                    user_agent=user_agent)

    def setSubreddit(self, nameSubreddit):
        self.__subreddit = self.__reddit.subreddit(nameSubreddit)

    def download(self, path, limit=None):
        count = 0

        for s in self.__subreddit.top(limit=limit):
            link = str(s.url)
            if link.endswith('jpg') or link.endswith('jpeg') or link.endswith('png'):
                urllib.request.urlretrieve(link, f"{path}/image{count}.jpg")
                count += 1
