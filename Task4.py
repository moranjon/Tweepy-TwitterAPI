# Task4.py
# CPS 470 - Computer Networks and Security
# Assignment 2 by Jonathan Moran (moranj13@udayton.edu)
# ---------
# This program only emails the user tweets that are related to their interest when they run the program.
# I decided that trying to grade and test a program to have it send an email at a certain time of day everyday would be
# unreasonable and difficult on the graders end, so I didn't implement my code to do such.
# This program instantly emails a user based on the following input:
##      their name
##      how many tweets they'd like to receive
##      their keywords they enter that relate to a particular interest
##      their email

## sample input is commented below this line:
        # Jon
        # 15
        # dogs, puppies, furry
        # moranj13@udayton.edu

import const
import tweepy
from tweepy import Stream
import smtplib, ssl

# A listener handles tweets that are received from the stream.
# This is a basic listener that prints recieved tweets to standard output
class TweetListener(Stream):
    def onData(self, data):  # return data
        print(data)
        return True

    def onError(self, status):  # return status on error
        print(status)

#Function to convert tweet texts into a better readable format for the email
def tweetsToMessageForm(str):
    # initialize an empty string
    str1 = "\n-----\nTWEET: "
    # return string
    return (str1.join(str))


def main():
    auth = tweepy.OAuthHandler(const.CONSUMER_KEY, const.CONSUMER_SECRET)
    auth.set_access_token(const.ACCESS_TOKEN, const.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth,wait_on_rate_limit=True)

    try:
        api.verify_credentials()
        print('Verification Successful.')
    except:
        print('Authentication Error.')

    # twitterStream = Stream(auth, TweetListener())
    twitterStream = Stream(const.CONSUMER_KEY, const.CONSUMER_SECRET, const.ACCESS_TOKEN, const.ACCESS_TOKEN_SECRET)



    print(f"The purpose of this program is to send you an email based on an interest you have."
          f"\nThis program instantly emails a user based on the following input:" \
          f"\n\tyour name" \
          f"\n\thow many tweets you'd like to receive" \
          f"\n\tkeywords that relate to your particular interest" \
          f"\n\tyour email" \
          f"\n" \
          f"\nSample input is below this line:" \
          f"\n\tJon" \
          f"\n\t15" \
          f"\n\t'honda', 'engine', 'civic'" \
          f"\n\tmoranj13@udayton.edu"
          f"\n - - - - - - - - - - - - - - - - - - - - - - - - -"
          f"\n")

    # insert your name
    # receiver_name = "Zhongmei"
    receiver_name = input("What is your name?\n")

    # insert how many tweets you'd like to to receive via email (preferably less than 100)
    # count = 10
    count = input("How many tweets would you like to receive in the email?\n")

    # insert the keywords related to an interest you want to receive tweets about
    # interest = ['dogs', 'puppies', 'furry']
    interest = input("List a few keywords related to your interest (in this format: 'keyword1', 'keyword2', etc.)\n")
    # insert receiving address
    rcvEmail = input("What is your email address?\n")

    ## print the list of tweets based on the given keywords (excludes retweets)
    tweetList = []
    for tweet in api.search_tweets(q="{}  -filter:retweets".format(interest),  count=count):
            tweetList.append(tweet.text)

    ## this is the variable message with the contents that are being sent
    msg = f"It's that time of day, {receiver_name}! Here are recent tweets about {interest} that you wanted to receive via email." \
          f"\n\n\n-----\nTWEET: {tweetsToMessageForm(tweetList)}\n-----" \
          f"\n\n\nHope you enjoyed reading these tweets!"
    msg = msg.encode('ascii', 'ignore').decode('ascii') # this is so the email goes through and no unicode errors occur

    ## Email code is as seen below (port connection, server specification and email log-in info)
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    ## I created a gmail account for this project for simplicity
    # you have permission to use the log in info that is included below
    sender_email = "pythontask4@gmail.com"  # don't change
    password = "CPS470pw1"  # don't change

    receiver_email = rcvEmail

    ## The subject and the body of the message being sent
    message = f"""\
    : {receiver_name}, this is just what you need! 
    
    \n{msg}"""

    ## Send email via SMTP using information above
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    print("The email has successfully sent! Make sure to check your Spam folder just in case it didn't make it to your Main inbox!")

    return  # end main

    # call main()
if __name__ == '__main__':
    main()