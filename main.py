import tweepy
auth = tweepy.OAuthHandler("CONSUMER KEY HERE", "CONSUMER KEY SECRET HERE")
auth.set_access_token("BEARER TOKEN HERE", "BEARER TOKEN SECRET HERE")
api = tweepy.API(auth)
print ("Tweet Message!")
print ("Twitter For?")
tweet = input("Conjure Up A Tweet ")
api.update_status(status =(tweet))
print ("Done!")
