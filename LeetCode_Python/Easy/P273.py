#########################################
##### Date: 15/10/2026              #####
##### Question Author: LeetCode     #####
##### Question Difficulty: Easy     #####
##### Program Author: Nathan Horder #####
#####                               #####
#########################################

### The question (Asked by Apple apparently)
### A fixed point in an array is an element whose value is equal to its
### index. Given a sorted array of distinct elements, return a fixed point,
### if one exists. Otherwise, return False

### For example, given [-6, 0, 2, 40], you should return 2
### Given [1, 5, 7, 8], you should return False.

## Intial Thoughts
## Fairly simple question, achievable via a FOR loop, no need for a function
## call as that may be redundant
## Ok, re-read it, it needs to be a function, for the return functionality

#%%
# Define the function
def IdentifyElementIndexMatch(arr_in):
    results = []

    # Loop 
    for idx in range(0,len(arr_in)):
        if (arr_in[idx] == idx): 
            results.append(idx)

    if (len(results) > 0): return results
    else: return False


#%%
if __name__ == '__main__':    
    ## Define the input array
    # Provided example A
    #arr_in = [-6, 0, 2, 40]

    # Provided example B
    #arr_in = [1, 5, 7, 8]

    ## Test for return confirmation
    #arr_in = [0, 1, 2, 3]

    ## Test for floats 
    arr_in = [-0.1, 1.1, 1.2, -1]

    print(IdentifyElementIndexMatch(arr_in))
