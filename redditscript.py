import praw

reddit = praw.Reddit(client_id='',
                     client_secret="", password='',
                     user_agent='USERAGENT', username='')

subreddit = reddit.subreddit('SUBREDDITNAME')
#buildapcsales

newPython = subreddit.new(limit=5)

for submission in newPython:
    print(submission)
