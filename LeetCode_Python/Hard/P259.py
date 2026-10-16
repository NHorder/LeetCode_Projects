##### Date: 15/10/2026              #####
##### Question Author: LeetCode     #####
##### Question Difficulty: Hard     #####
##### Program Author: Nathan Horder #####
#####                               #####
#########################################

## Ghost is a two-person word game where players alternate appending letters to a word. 
## The first person who spells out a word, or creates a prefix for which there is no possible
## continuation, loses. Here is a sample game:

### Player 1: g
### Player 2: h
### Player 1: o
### Player 2: s
### Player 1: t [loses]
### Given a dictionary of words, determine the letters the first player should start with, such 
### that with optimal play they cannot lose.

### For example, if the dictionary is ["cat", "calf", "dog", "bear"], the only winning start 
### letter would be b.


## So my first thoughts on this problem is that you need to search for two items
## A) Duplicates  B) Even items
## If something has no duplicate starting letter AND is even, it's valid
## If it has a duplicate that is odd, then it's not valid

## I would use a dictionary to do this, put the starting letter in the dictionary with a bool value
## Letters would only be added of even items, and would be true if they DO NOT have a duplicate
## 
## Resulting in :  [letterOfEvenWord : doesNotHaveDuplicates]

## Also, the input isn't a dictionary... it's a list or array

## After an intial implementation attempt using this approach, I reliased that I could probably achieve this
## without using a dictionary, reducing the spatial requirements.

#%%
# Define the input dictionary
input_dict = ["Hello","Hello No", "There","Your"]

# Define the optimal word
optimal_word = ""

# Loop through all items in the list
for item in input_dict:

    # CHeck if the length of the item is odd AND if the start is the same as the optimal word
    # If so, set the optimal word to "" (Blank), as the original word is no longer optimal
    # .lower is used to ensure comparison regardless of case
    if (len(item) % 2 != 0 and optimal_word != "" and item[0].lower() == optimal_word[0]): optimal_word = ""

    # Else, assume the item is EVEN in length, and check to see if it has less words than the optimal one
    # with a check to see if the optimal word is empty or not- and update if true
    elif (optimal_word == "" or len(item) < len(optimal_word)): optimal_word = item.lower()

print(optimal_word[0])
# %%
