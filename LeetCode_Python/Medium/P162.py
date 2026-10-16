##### Date: 16/10/2026              #####
##### Question Author: LeetCode     #####
##### Question Difficulty: Medium     #####
##### Program Author: Nathan Horder #####
#####                               #####
#########################################

### Given a list of words, return the shortest unique prefix of each word
### For example, given the list
### - dog
### - cat
### - apple
### - apricot
### - fish

### Return the list
### d
### c
### app
### apr
### f

## So my intial thoughts is that this will take O(n^2) time
## As you would need to compare a value to each other
## I.e: Does 'd' exist, oh it does? does 'do' exist? And so on

## But I feel like there is a faster approach
## For now, I'll implement the O(n^2) approach, see if I can figure out a faster approach

## Ok, this is a harder question than I intially thought due to it's potential conditions
## I.e  dig dodge dodger,  it would need to output di, dodge dodger

## Could I use a dictionary instead?
## I.e [word: prefixIdx]

#%%

# Define input(s)
in_list = ["dog","cat","apple","apricot","fish"]
#in_list = ["dig","dodge","dodger","digger","dog", "doggreat"]
#in_list = ["dog", "doggreat"]

# Define the function
def ShortedUniquePrefix(in_list):
    # Define the output list
    out_list = []

    for item in in_list:

        # Define the expected output
        final_prefix = item[0]

        # Loop through next set of items
        for second_item in in_list:

            # If it finds itself, skip this loop
            if (item == second_item): continue

            # Reset index to 1, (Not 0 as final prefix = item[0])
            idx = 1

            # Set prefix to first letter
            prefix = item[0]

            # Loop while true, to determine how many are duplicates
            while True:
                
                # If the index is equal to or larger than the number of letters, then break the loop
                if (idx >= len(item)): break

                # Else, extend the prefix
                prefix += item[idx]

                # If the idx is more than the second item, break as they can't be compared
                if (idx >= len(second_item)): break


                # If the whole sentence is the same, then increase the index
                ## This remains functional as I'm checking all previous characters
                ## if the idx+1 > len(list) it would still work as it would print what is in the list
                if (item[:idx+1] == second_item[:idx+1]): idx += 1

                # Otherwise break
                else: break

            # If the length of the updated prefix is more than the final prefix, update it
            if (len(prefix) > len(final_prefix)): final_prefix = prefix

        # Add the final prefix to the output list
        out_list.append(final_prefix)

    return out_list

print(ShortedUniquePrefix(in_list))


