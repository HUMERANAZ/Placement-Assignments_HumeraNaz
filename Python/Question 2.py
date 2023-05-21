'''
Question 2: -
Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if
he can remove just one character at the index in the string, and the remaining characters will occur the same
number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO .
Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
an explanation for the same.
Example input 1 - s = “abc”. This is a valid string because frequencies are { “a”: 1, “b”: 1, “c”: 1 }
Example output 1- YES
Example input 2 - s “abcc”. This string is not valid as we can remove only 1 occurrence of “c”. That leaves
character frequencies of { “a”: 1, “b”: 1 , “c”: 2 }
Example output 2 - NO
'''

#Ans

def is_valid_string(string):
    
    char_count={}
    
    #finding the frequency of each character in string
    for char in string:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    
    #list of characters frequency
    char_count_list = list(char_count.values())
    
    #finding unique frequency
    frequencies=set(char_count.values())
    
    #if all characters have same frequency then unique frequency will be 1
    if len(frequencies)==1:
        return "Yes"
    
    
    if len(frequencies)==2:
        # Check if removing one character can make all frequencies the same
        
        max_freq = max(frequencies)
        min_freq = min(frequencies)
        
        if char_count_list.count(min_freq) == 1 and min_freq == 1:
            # Removing a character with the minimum frequency makes the string valid
            return "YES"
        if char_count_list.count(max_freq) == 1 and max_freq - min_freq == 1:
            # Removing a character with the maximum frequency reduces the frequency to match the others
            return "NO"

    return "NO"

s1 = "abc"
result1 = is_valid_string(s1)
print(result1)

s2 = "abcc"
result2 = is_valid_string(s2)
print(result2)



#Additional Test Case:

#Case 1.:

s3 = "aabccdd"
result3 = is_valid_string(s3)
print(result3)

'''
Explanation: In above string all characters except 'b' has equal frequency i.e {a:2,b:1,c:2,d:2}
and 'b' frequency is one which can be removed as one character so it is a valid string and output is "Yes"
'''

#Case 2.:
s4 = "aaabdddd"
result4 = is_valid_string(s4)
print(result4)

'''
Explanation: In above string all characters has different frequecny so i.e. {a:3,b:1,d:4} so it is not valid string.
Output is "NO" 
'''