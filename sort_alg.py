import time
import numpy as np
#Define function that creates an array of random numbers within a range and of a given length
def makearr(st, en, ra):
    '''Input:
        st = lowest number that our array could have
        en = largest number our array could have
        ra = length of our array
       Output:
        random_array = array of random integer numbers between numbers st and en of lenght ra
    '''
    if en-st<ra:
        print("try again making sure that en-st>ra")
    if en-st>ra:
        random_array = np.random.randint(st, en, ra)
        return random_array

#Defining function that finds the minimum value of the array
def find_min(arr):
    '''Input: array
       Output: index and value of the array element with the lowest value
    '''
#take the first element as our reference or control for the guess absolute minimum
    minn = arr[0]
    #compare each array element to the first element on the array
    for test in arr:
        if test < minn: #if the test number is lower than the first array element (our "control min")
            minn = test #update the minimum value with the array element being tested
    #fin the index of the minimum number within the array
    ind = np.where(arr == minn)[0][0]
    #print the minimum value and its corresponding index
    #print("The minimum value is: "+str(minn)+". The index within the array is: "+str(ind))
    return minn, ind

#Defining a sorting function
def sort(arr0):
    '''Input: unsorted array
       Output: sorted array
    '''
    #obtain length of array
    r = len(arr0)
    #create the new future sorted array
    aso = [0]*r
    for j in range(r):
        #find minimum of the original array r times
        mi, ind = find_min(arr0)
        #assign the minimum value of that iteration to the index j of the sorted array
        aso[j] = mi
        #delete that index from the original array 
        arr0 = np.delete(arr0,ind)       
    return aso


#testing our sorting algorithm
a = makearr(0, 150, 5)
b = sort(a)
print(a,b)

#comparing the runtime between our sorting algorithm and python's ibuilt one
t0 = time.perf_counter()
b = sort(a)
t0 = time.perf_counter()-t0

t1 = time.perf_counter()
c = np.sort(a)
t1 = time.perf_counter()-t1

print("Our function takes "+str(t0)+"s. Python's inbuilt sort function takes "+str(t1)+"s.")
