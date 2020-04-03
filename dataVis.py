import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("tweet_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

#create polarity and subjectivity list list
polarityList = []
subjectivityList = []
tweetString = ""

for tweet in tweetData:
	#print("Tweet text: " + tweet["text"])
    tweetBlob = TextBlob(tweet["text"])
    #sentiment(polarity, subjectivity)
    polarityList.append(tweetBlob.sentiment.polarity)
    subjectivityList.append(tweetBlob.sentiment.subjectivity)
    tweetString += tweet["text"]

tweetString = TextBlob(tweetString)

tweetWords = {}

for word in tweetString.words:
    tweetWords[word] = 1


polarityAvg = 0
for value in polarityList:
    polarityAvg += value
print(polarityAvg/len(polarityList))
#print(sorted(polarityList))

subjectivityAvg = 0
for value in subjectivityList:
    subjectivityAvg += value
print(subjectivityAvg/len(subjectivityList))
#print(sorted(subjectivityList))


#print histogram

plt.hist(polarityList, bins=[-0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
#plt.show()






# Textblob sample:
#tb = TextBlob("You are a brilliant computer scientist.")
#print(tb.polarity)


# Next we want to open the JSON file. We tag this file as
# "r" read-only because we are only going to look at the data.
#tweetFile = open("tweet_small.json", "r")

# We use the JSON library to get data from the file as JSON data.
#tweetData = json.load(tweetFile)

# We can close the file now that we have locally stored the data.
#tweetFile.close()



# We then print the data of ONE tweet:
# the [0] denotes the *first* tweet object.
# We access parts of the tweet using ["NameOfPart"].
##print("Tweet id: ", tweetData[0]["id"])

# printing the text object of the tweet
##print("Tweet text: ", tweetData[0]["text"])

#Two options for looping through the twwets:

# Option 1, here, we're using index and
# counting the number of tweets in the tweetData
# using the python len() function.
#for idx in range(len(tweetData)):
#	print("Tweet text: " + tweetData[idx]["text"])

# Option 2, Python lets you get objects
# directly without having to use an index.
##for tweet in tweetData:
##	print("Tweet text: " + tweet["text"])
