'''
    Python Twitter API Sentiment Analysis by Eanna Curran
    Program which connects to the Twitter API and calculates the polarity of tweets containing certain keyword and records results

'''


from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from textblob import TextBlob
import time

ckey = 'wr40uoqlIEf2I8EzcmKrCnfbP'
csecret =  'TJB3pBEHTCSU9wH3fLoj2GQsJOYzO7oZ6i6T3ftb3X4SVIjpXf'
atoken = '750831686934466561-lTFBkDZiqY971uDbixIrPVbDw583A1D'
asecret = 'bG1gEG1xYI9cnhwJ9gqXKIxMPh5TeVsR5Td8LCGZ1QiYp'

total = 0
tally = 0
start = time.time()

# Calculates average polarity and records results
def average_polatity(total, tally):
    average = 10 * (total / tally)
    average = round(average, 2)
    print(average)
    saveFile = open('TwitterAverageSentiment.csv', 'a')
    saveFile.write(str(average))
    saveFile.write('\n')
    saveFile.close()

# Calculates total polarity from tweets every 30 seconds
def total_polatity(polarity):
    global total
    global tally
    global start
    total += float(polarity)
    tally += 1
    if time.time() - start > 30:
        average_polatity(total, tally)
        total = 0
        tally = 0
        start = time.time()

    
# Cleans Twitter data, records tweets and calls to calculate polarity of tweet
class listener(StreamListener):

    def on_data(self, data):


        try:
            tweet = data.split(',"text":"')[1].split(',"source":"')[0]

            if 'https' in tweet:
                try:
                    tweet = data.split(':{"full_text":"')[1].split(',"display_text_range":')[0]
                except:
                    tweet = data.split(',"text":"')[1].split(',"source":"')[0]

            if tweet[-7:].encode('utf-8') == b'\u2026"':
                try:
                    tweet = data.split(':{"full_text":"')[1].split(',"display_text_range":')[0]
                except:
                    tweet = data.split(',"text":"')[1].split(',"source":"')[0]

            for word in tweet.split():
                if word[:4] == 'http':
                   tweet = tweet.replace(word, '')
                if word[:1] == '@':
                   tweet = tweet.replace(word, '')
                if word[:2] == b'\u':
                   tweet = tweet.replace(word, '')
                if word[:2] == b'\n':
                   tweet = tweet.replace(word, '')
                if word[:2] == '#':
                   tweet = tweet.replace(word, '')
        
            tweet = tweet.encode('ascii', 'replace').decode('unicode-escape').replace('\n', '')
            
            analysis = TextBlob(tweet)
            sentiment = str(analysis.sentiment)
            polarity = str(analysis.sentiment.polarity)
            subjectivity = str(analysis.sentiment.subjectivity)

            saveData = str(time.time()) + '::' + tweet + sentiment
            saveFile = open('TwitterDataBase.csv', 'a')
            saveFile.write(saveData)
            saveFile.write('\n')
            saveFile.close()

            total_polatity(polarity)

            return True

        except BaseException as e:
            pass
            
    def on_error(self, status):
        print(status)

# Acceses the Twitter API
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

# Steams tweets from specific keyword
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Ireland"])

