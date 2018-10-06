from textblob import TextBlob
import csv


def sentiment_to_label(sentiment):
    if -1 <= sentiment.polarity <= -0.5:
        return 'extremely negative polar'
    elif -0.5 < sentiment.polarity < 0.5:
        return 'kind of objective'
    elif 0.5 <= sentiment.polarity <= 1:
        return 'extremely positive polar'
    else:
        return 'WAT?!'


tweets = list()
tweets.append(TextBlob("My mother is so preety and beautiful"))
tweets.append(TextBlob("In last year our income increased up to 2 billion $$$"))
tweets.append(TextBlob("Expect that, this object will not response in the way you wanted"))
tweets.append(TextBlob("I would love to see Johny Cash"))
tweets.append(TextBlob("This hamster is ugly"))

labels = list()
sentiments = list()
for tweet in tweets:
    sentiments.append(tweet.sentiment)
    labels.append(sentiment_to_label(tweet.sentiment))

tweets_with_sentiments = zip(tweets, sentiments, labels)

# Write to *.csv
with open('results.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';')
    csv_writer.writerows(tweets_with_sentiments)


