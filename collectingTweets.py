#Import Statements
import tweepy 
import csv

#Twitter API credentials
consumer_key = "voVmM67lWMJKIdektrW59WYuF"
consumer_secret = "EsPXnZCLlgAPCPLTMXkdFhozsqJR6tI1CukkMILv5dK1rZvzju"
access_key = "1354959928562225154-5CPcMQRiB4bgRubALF0dZNst34ilhe"
access_secret = "g42NySe0lXGlQLkanbfx5w8grvQShkkr5K3n9TFycvBcj"

#Collecting the Tweets or a Particular User
def get_all_tweets(screen_name):

    #Initializing Tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #Setting up list for Tweets
    alltweets = []  

    #Collect most recent tweets 
    new_tweets = api.user_timeline(screen_name = "BiggieC88585117",count=200)

    #Save most recent tweets
    alltweets.extend(new_tweets)

    #Save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #Continue collecting Tweets until there's no more left to take 
    while len(new_tweets) > 0:

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = "ClearGreenDay",count=200,max_id=oldest)

        #Save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

    #Making Tweets into a 2D Array
    textTweets = [[tweet.text] for tweet in alltweets]
    timeTweets = [[tweet.created_at] for tweet in alltweets]
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]

    #Writing all Information to File 
    with open(f'new_{screen_name}_tweets.csv', 'w', encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)

    #Writing only Tweets to File
    with open ("tweetsData.csv", "w", encoding = "utf-8") as file:
        writer2 = csv.writer(file)
        writer2.writerows(textTweets)

    #Writing only Time Stamps to File
    with open ("timeData.csv", "w", encoding = "utf-8") as nFile:
        writer3 = csv.writer(nFile)
        writer3.writerows(timeTweets)

    pass


if __name__ == '__main__':
    #Passing Twitter Username of Account 
    get_all_tweets("J_tsar")