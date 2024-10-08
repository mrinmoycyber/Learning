# Sort a list of tuples based on the second element of each tuple without using Python's built-in sort function

def bubble_sort_tuples(tuples_list):
    n = len(tuples_list)
    #Traverse through all the elemetns in the list
    for i in range(n):
        #last i elements are already in place
        for j in range(0, n-i-1):
            #Compare the second element in each tuple 
            if tuples_list[j][1] > tuples_list[j+1][1]:
                #Swap if the element found is greater
                tuples_list[j], tuples_list[j+1] = tuples_list[j+1], tuples_list[j]
                
tuples_list = [(1, 4), (3, 2), (5, 1), (7, 3)]
print("Given:", tuples_list)

bubble_sort_tuples(tuples_list)
print("Sorted list of tuples by second element:", tuples_list)

                
            