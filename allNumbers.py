"""    STSTIC VARIABLE CREATION    """
import timeit

start = timeit.default_timer()

def static():
        static.i += 1
static.i = 0               # static variable


#------------------------------------------------------------------#

                        # Global variables
arr = []
a = []
Range = 0
no = 0
b = []

#------------------------------------------------------------------#
"""    RECURSION    """

def fun(s):
        if(s>Range):
                return;
        else:
                for c in range (0,no,1):
                            if((((s*10)+a[c])<=Range)&(((s*10)+a[c])>=0)):
                                t = (s*10)+a[c]
                                arr.append(t)
                                b.append(arr[static.i])
                                static()
                                if(b[static.i-1]!=0):
                                        fun(b[static.i-1])
                            else:
                                return;


# Recursive functions ends

#-------------------------------------------------------------------#


"""       Sorting       """

def sort(x):
        for i in range (0,len(x),1):
                small = x[i]
                loc = i
                for j in range (i+1,len(x),1):
                        if(small>x[j]):
                                small = x[j]
                                loc = j
                if(loc != i):
                        x[loc] = x[i]
                        x[i] = small


#-------------------------------------------------------------------#
                        
#####################################################################
                        
"""       Main function      """



                                                
no = int(input("\nEnter the no. of digits for combination: "))
print ("\nEnter %i different digites, for combination:  \n"%(no))
for m in range (0,no,1):
    a.append(int(input()))

sort(a)

Range = int(input("\nEnter the range: "))

start2 = timeit.default_timer()
fun(0)
stop2 = timeit.default_timer()

sort(arr)

print ("\nTotal no. of possible combinations: %i" %(len(arr)))
print ("Combinations are:-")

for p in range (0,len(arr),1):
        print (arr[p])

#input("\nPress ENTER to get exit!")


stop = timeit.default_timer()

print ("\n\nTime taken for the execution of complete program: %f seconds"%(stop - start) )
print ("Time taken in finding all possible combinations: %f seconds"%(stop2 - start2) )
######################################################################
