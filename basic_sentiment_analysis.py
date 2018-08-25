"""
keep running counts of good and bad words, if good words > bad words, then the tweet is good
otherwise it's bad

"""
tweet_string = "Thanks to the historic TAX CUTS that I signed into law, your paychecks are going way UP, " \
               "your taxes are going way DOWN, and America is once again OPEN FOR BUSINESS!"
tweet_words = tweet_string.split()
number_of_words = len(tweet_words)

# counters for good and bad words
number_of_good_words = 0
number_of_bad_words = 0

# arrays of words we're counting as 'good' and words we're counting as 'bad'
good_words = ["Thanks", "historic", "paychecks"]
bad_words = ["taxes"]

for word in tweet_words:
    print(word)
    # if the word is in the array of good words
    if word in good_words:
        # increase the count of good words by 1
        number_of_good_words += 1
    # if the word is in the bad words array
    elif word in bad_words:
        # increment the bad words couter by 1
        number_of_bad_words += 1

print("There are " + str(number_of_good_words) + " 'good' words in this tweet.")
print("There are " + str(number_of_bad_words) + " 'bad' words in this tweet.")

if number_of_good_words > number_of_bad_words:
    print("There were more good words than bad words in the tweet.")
else:
    print("There were more bad words than good words in the tweet.")