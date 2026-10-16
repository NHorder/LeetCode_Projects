##### Date: 16/10/2026              #####
##### Question Author: LeetCode     #####
##### Question Difficulty: Medium     #####
##### Program Author: Nathan Horder #####
#####                               #####
#########################################

### Implement a 2D iterator class. It will be intialized with an array of arrays
### and should implement the following methods
### - next(): retursn the next eelemtn in the array of arrays. If there are no more elements, raise an exception
### - has_next(): returns whether or not the iterator still has elements left

### For edxample, given the input [[1,2],[3],[],[4,5,6]] calling next repeatedly should output
### 1, 2, 3, 4, 5, 6
### Do not use flattern or otherwise clone hte arryas. Some of the arrays can be empty

## Initial thoughts are that the class needs to contain two indexes, the current index and current sub-index
## to keep track of the location. 


#%%
class Iterate():

    def __init__(self,input_arr):
        # Define input arra
        self.arr = input_arr

        # Define current indexs (main and sub)
        # Could be later modified to accept an array of any dimensionality, though use of a list
        self._current_idx = 0   
        self._current_sub_idx = 0

    def next(self):

        # Check if it has another item
        if (self.has_next()):

            # Collect the value
            return_val = self.arr[self._current_idx][self._current_sub_idx]

            # Increment index
            self._current_sub_idx += 1

            # Return the value
            return return_val

        # If there are no more items, raise an exception
        else:
            raise Exception

    def has_next(self):

        ## The Idea here is that the current index is the next value
        ## So, I just need to check if the next value exists, which I can do with a little recursion

        # Check if the current index exists and is valid
        if (self._current_idx < len(self.arr)):

            # Check if the sub index exists and is valid
            # If so, return True
            if (self._current_sub_idx < len(self.arr[self._current_idx])):
                return True

            # Otherwise, increment the index and reset sub idx
            # As the sub idx value has been exceeded or a sub-dict does not exist
            self._current_idx += 1
            self._current_sub_idx = 0

            # Call this function with the updated values
            return self.has_next()

        # Else return false
        return False

        




#%%
input_arr = [[1,2],[3],[],[4,5,6]]
i = Iterate(input_arr)
#%%
i.next()
