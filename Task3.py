import math

# This is merge sort algorythm, it's complexity is nLogn, which is one of the best complexities (and best as far as i know for sorting)
# we split array to smaller arrays untill we get arrays with size of 1, and after that we merge them, using rule of the smallest of pair



# Brief- Sorts array using merge sort
#
# sorting_arr- array to be sorted
#
# return sorted array
#
def MergeSort(sorting_arr):

    # Calculate splitter (amount of elements in left array and right array, left.size>right.size)
    splitter=math.ceil(len(sorting_arr)/2)
    left_arr=None
    right_arr=None
    # If splitter is ==1, then it means that we have individual elements, else we continue recursevly splitting
    if(splitter>1):
        # fill left and right arrays
        left_arr=sorting_arr[0:splitter]
        right_arr=sorting_arr[splitter:len(sorting_arr)]
        # sort them (recursion)
        MergeSort(left_arr)
        MergeSort(right_arr)

        # merge left and right arrays decreasing their sizes, using the smallest posiible in pair
        sorting_arr.clear()
        while (len(left_arr)>0 and len(right_arr)>0):
            if(left_arr[0]<right_arr[0]):
                sorting_arr.append(left_arr.pop(0))
            else:
                sorting_arr.append(right_arr.pop(0))
        
        # If some of the array has leftovers, append them
        sorting_arr+=left_arr
        sorting_arr+=right_arr

        #return sorted array
        return sorting_arr
    

    # If len is 1, then it means, that previous step was uneven, so we just return single element
    if(len(sorting_arr)==1):
        return sorting_arr
    
    
    # Sort two numbers    
    if(sorting_arr[0]>sorting_arr[1]):
        pop=sorting_arr[0]
        sorting_arr[0]=sorting_arr[1]
        sorting_arr[1]=pop

    return sorting_arr



sorted_arr=MergeSort([1,2,5,32,43,123,4,3,1,2])
print(sorted_arr)

sorted_arr=MergeSort([1,1,1,1,1,1,1,1,1,1])
print(sorted_arr)

sorted_arr=MergeSort([1,2,5,32,43,123,4,3,1])
print(sorted_arr)

sorted_arr=MergeSort([1,1,2,2,3,4,5,32,43,123])
print(sorted_arr)

sorted_arr=MergeSort([123,43,32,5,4,3,2,2,1,1])
print(sorted_arr)

