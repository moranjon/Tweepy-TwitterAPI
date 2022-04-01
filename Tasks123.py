# Tasks123.py
# Assignment 2 by Jonathan Moran (moranj13@udayton.edu)

import const
import tweepy
from tweepy import Stream


# A listener handles tweets that are received from the stream.
# This is a basic listener that prints recieved tweets to standard output
class TweetListener(Stream):
    def onData(self, data):  # return data
        print(data)
        return True

    def onError(self, status):  # return status on error
        print(status)


def main():
    ## setting up the authentication for the API with my specific keys
    auth = tweepy.OAuthHandler(const.CONSUMER_KEY, const.CONSUMER_SECRET)
    auth.set_access_token(const.ACCESS_TOKEN, const.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth,wait_on_rate_limit=True)

    ## attempts verifying the API credentials
    try:
        api.verify_credentials()
        print('Verification Successful.')
    except:
        print('Authentication Error.')

    #twitterStream = Stream(auth, TweetListener())
    twitterStream = Stream(const.CONSUMER_KEY, const.CONSUMER_SECRET, const.ACCESS_TOKEN, const.ACCESS_TOKEN_SECRET)
    #users = api.lookup_users(screen_name={"github", "twitter"})

    ## look up users from the API
    users = api.lookup_users(screen_name={"AnnieWesner", "swavey_jake"})


    print("TASK 1 ----------------") #printing user information and details

    ## loop for grabbing information about each user
    for user in users:
        print("\nUser name: ", user.name)
        print("Screen name: ", user.screen_name)
        print("User ID: ", user.id)
        print("Location: ", user.location)
        print("User description: \n", user.description)
        print("The number of followers: ", user.followers_count)
        print("The number friends: ", user.friends_count)
        # print("Favorites count: ", user.favourites_count)
        print("The number of Tweets: ", user.statuses_count)
        print("User Url: ", user.url)

    print("\nTASK 2 ----------------")

    ## loop for each user
    for user in users:
        print("\nScreen Name: ", user.screen_name)
        print("Latest 20 followers: ")

        count = 20
        ## grab the 20 most recent followers of my two inputted users
        for follower in api.get_followers(screen_name = user.screen_name, count = count):
            print('follower: ' + follower.screen_name)

        # check mutual friendship for each of the 20 followers
        print("Friends (mutual following): ")

        # set screen name of the account
        source_screen_name = user.screen_name

        ## check through latest 20 followers to see if they also are followed by the user ===> then they are mutual friends
        for follower in api.get_followers(screen_name = user.screen_name, count = count):
            ## set follower as target
            target_screen_name = follower.screen_name
            ## ** checking if following is mutual (bidirectional) between the inputted user and specific follower **
            friendship = api.get_friendship(source_screen_name=source_screen_name, target_screen_name=target_screen_name)
            if friendship[0].followed_by == True and friendship[1].followed_by == True:
                print('mutual friend: ' + target_screen_name)

    print("\nTASK 3 ----------------")

    newCount = 50
    #3.a  ## print tweets that include specific keywords
    print('\nTask 3.a --- specific keyword')
    for tweet in api.search_tweets(q="[Ohio, weather]", count = newCount):
        print('Tweet: ' + tweet.text)

    #3.b  ## print tweets based on geolocation
    print('\nTask 3.b --- Dayton Geolocation')
    for tweet in api.search_tweets(q= '', geocode= ('39.758949,-84.191605,25mi'), count = newCount):
        print('Tweet: ' + tweet.text)

    return  # end main


# call main()
if __name__ == '__main__':
    main()
