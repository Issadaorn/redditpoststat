import praw
import pandas as pd
import datetime

posts = []
name = 'streaming'
num_posts = 1000
reddit = praw.Reddit(client_id='my_client_id',
                     client_secret='my_client_secret',
                     user_agent='my_user_agent')


subreddit_name = reddit.subreddit(name)

for post in subreddit_name.new(limit=num_posts):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
created = posts['created']
created = created.apply(lambda x: datetime.datetime.fromtimestamp(x))
posts['created'] = created

print(posts)
posts.to_csv("Posts.csv", index=True)

def count_posts_inlast_week(posts):
    last_week = datetime.datetime.now() - datetime.timedelta(days=7)
    return len(posts[posts['created'] > last_week])

print (count_posts_inlast_week(posts))