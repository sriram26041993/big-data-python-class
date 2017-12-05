#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "925147187184635904-DdhQn8xZKPVFwHb68mYUHuhzpi8Anzu"
access_token_secret = "8I4Lg5fz5sNPawKccZXpjQCu4azXEa3UbFNjvyAe2xTWY"
consumer_key = "KT6cdia0sVGwrmyqX0m4xXbac"
consumer_secret = "ovXZkyp7k4jih8LalVRVHfLCxZTn9TztolHmMCvbBtOyDLLVYw"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'ATT', 'Newyork', 'wirless', 'DTV' , 'Uverse'.
    stream.filter(track=['verizon','Verizon', 'wireless','wls','wireline','wln', 'TV','Tv','tv' , 'Uverse','uverse','UVERSE'])