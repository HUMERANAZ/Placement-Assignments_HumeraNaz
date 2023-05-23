#Ans 1.

def highest_frequency_word_len(string):
    # Splitting the string into words
    words_list = string.split()

    # Count the frequency of each word
    word_counts = {}
    for word in words_list:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1

    # Find the word with the highest frequency
    max_frequency = max(word_counts.values())
    highest_frequency_words = [word for word, count in word_counts.items() if count == max_frequency]

    # Find the length of the highest-frequency word
    highest_frequency_word_length = len(highest_frequency_words[0])

    return highest_frequency_word_length



string = "write write write all the number from from from 1 to 100"
result = highest_frequency_word_len(string)
print(result)

#Example output - 5
#Explanation - In above stirng the most frequent words are “write” and “from” and "write" has maximum character length so output will be 5.



#Additional Test Cases:


# Case 1: Testing with a string that contains multiple words with the same highest frequency:

string = "apple orange banana apple orange banana apple"
result = highest_frequency_word_len(string)
print(result)

"""Explanation:
In this case, the words "apple" and "orange" both appear three times, which is the highest frequency among all the words. 
The length of both "apple" and "orange" is 5.
Since the program returns the length of the first highest-frequency word, it returns 5 as the output.
"""


# Case 2 : Testing with a string that contains only one word:

string = "hello"
result = highest_frequency_word_len(string)
print(result)

"""
Explanation:
In this case, there is only one word in the string, so it is also the highest-frequency word. 
The length of the word "hello" is 5, so the program returns 5 as the output.

"""