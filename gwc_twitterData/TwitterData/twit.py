'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("tweet-small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

# Textblob sample:
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)
print(tb.sentiment)


polarity = []
subjectivity = []

for tweet in tweetData:
    tb = TextBlob(tweet["text"])
    polarity.append(tb.polarity)
    subjectivity.append(tb.subjectivity)

averagePolarity = sum(polarity) / len(polarity)
averageSubjectivity = sum(subjectivity) / len(subjectivity)

print ("Average Polarity: ", averagePolarity)
print ("Average Subjectivity: ", averageSubjectivity)



plt.plot(polarity, subjectivity, 'ro')
plt.xlabel("Polarity")
plt.ylabel("Subjectivity")
plt.title("Tweet Polarity vs Subjectivity")
plt.axis([-1.1, 1.1, -0.1, 1.1])
plt.grid(True)
plt.show()

allTweets = ""
for tweet in tweetData:
    allTweets += tweet["text"]

blob = TextBlob(allTweets)

# filteredWords[word] = count

wordCount = {}
skipWords = ["https", "about"]
for word in blob.words:
    if word in skipWords:
        continue
    if len(word) < 4:
        continue
    wordCount[word.lower()] = blob.word_counts[word.lower()]


wordcloud = WordCloud().generate_from_frequencies(list(wordCount.items()))
plt.imshow(wordcloud, interpolation = "bilinear")
plt.axis("off")
plt.show()
