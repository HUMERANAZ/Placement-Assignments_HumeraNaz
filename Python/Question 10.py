#Ans 10

import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize

def count_pos_tags(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Perform Part-of-Speech tagging
    tagged_words = pos_tag(words)
    
    # Initialize counts for each part-of-speech
    verb_count = 0
    noun_count = 0
    pronoun_count = 0
    adjective_count = 0
    
    # Iterate over the tagged words and count the occurrences of each part-of-speech
    for word, tag in tagged_words:
        if tag.startswith('V'):  # Verb tags start with 'V'
            verb_count += 1
        elif tag.startswith('N'):  # Noun tags start with 'N'
            noun_count += 1
        elif tag.startswith('PRP'):  # Pronoun tags start with 'PRP'
            pronoun_count += 1
        elif tag.startswith('JJ'):  # Adjective tags start with 'JJ'
            adjective_count += 1
    
    # Create a dictionary to store the counts
    pos_counts = {
        'Verbs': verb_count,
        'Nouns': noun_count,
        'Pronouns': pronoun_count,
        'Adjectives': adjective_count
    }
    
    return pos_counts

# Example usage
text = "I love eating pizza."
counts = count_pos_tags(text)
print(counts)


#Additional Test Cases:

#Case 1:

text = "I enjoy reading books. They transport me to different worlds. The colorful illustrations make the stories come alive."
counts = count_pos_tags(text)
print(counts)

'''
Explanation: The paragraph contains 3 verbs ("enjoy", "reading", "make"), 
4 nouns ("books", "worlds", "illustrations", "stories"), 
4 pronouns ("I", "me", "They", "the"), and 
3 adjectives ("different", "colorful", "alive").
'''


#Case 2:

text = "She quickly ran to the beautiful garden and picked some fresh flowers."
counts = count_pos_tags(text)
print(counts)

'''
Explanation: The sentence contains 1 verb ("ran"), 
3 nouns ("She", "garden", "flowers"), 
1 pronoun ("some"), and 
2 adjectives ("beautiful", "fresh").
'''

