our_list = [1,4,6,3,0,9,18]

#backwards sorting

def insertion_sort(a_list):

    total = 0
    for i in range(1,len(a_list)):

        key = a_list[i]
        j = i-1 
    
        while j>= 0 and key>a_list[j]: #this means we wont get an indexerror
            #while this is greater than the element before it
            a_list[j+1] = a_list[j]
            j -= 1 
            total += 1
        
        a_list[j+1] = key
        return a_list, total

print(insertion_sort(our_list))

#best case scenario is a sorted list, worst case scenario is a list that is reverse sorted
# O(n^2)