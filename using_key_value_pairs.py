"""

using key value pairs so we can assign more variable ratings to words instead of just 'good' or 'bad'
we can assign a numerical value to start getting a sense of a range of each category

To evaluate the good or bad score of a tweet, we first split our tweet.
We then associate each word with positive and negative values, respectively, using a dictionary.

Finally, we caculate the average word weight of a tweet, and decide if it's a good or bad one
based on that.

"""


# define a function that we'll use later in the code to break a tweet down into individual words
def get_words(tweet):
    return tweet.split()


# key value pairs for the words we want to rate
word_weights = {"Thanks": 1.0, "historic": 0.5, "paychecks": 0.8, "taxes": -1.0}


# define a function to get the average rating of words in the tweet
def get_average_word_weight(list_of_words):
    number_of_words = len(list_of_words)
    # instantiate holder for the word weight
    sum_of_word_weights = 0.0
    for word in list_of_words:
        # if the word is in our ratings key value pair list
        if word in word_weights:
            sum_of_word_weights += word_weights[word]

    return sum_of_word_weights / number_of_words


tweet_string = "Thanks to the historic TAX CUTS that I signed into law, your paychecks are going way UP, " \
               "your taxes are going way DOWN, and America is once again OPEN FOR BUSINESS!"
words = get_words(tweet_string)
average_tweet_weight = get_average_word_weight(words)


print("The weight of the tweet is " + str(average_tweet_weight))

if average_tweet_weight > 0:
    print("The tweet is mostly good.")
else:
    print("The tweet is mostly bad")
