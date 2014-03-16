from ys_twitter import TWTR_OAUTH

t = TWTR_OAUTH.twitter_api
print repr(t.followers.list())
