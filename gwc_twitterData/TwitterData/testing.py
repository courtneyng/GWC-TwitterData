
for tweet in tweets:
    polarity.extend(tb.polarity)
    polarity.extend(tb.sentiment)

    for word in blob.words:
        wordCount[word.lower()] = blob.word_counts[word.lower()]

        plt.hist(polarity, bins = [-1, -0.5, 0, .5, 1])
        plt.xlabel('Polarities')
        plt.ylabel('Number of Tweet')
        plt.title('Histogram of Tweet Polarity')
        plt.axis([-1.1, 1.1, 0, 100])
        plt.grid(True)
        plt.show()

        plt.hist(subjectivity, bins = [-1, -0.5, 0, .5, 1])
        plt.xlabel('Subjectivities')
        plt.ylabel('Number of Tweet')
        plt.title('Histogram of Tweet Subjectivity')
        plt.axis([-1.1, 1.1, 0, 100])
        plt.grid(True)
        plt.show()
