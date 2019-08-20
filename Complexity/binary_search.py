#find median of list, assuming already ordered and then if element is less than median, gets rid of the other half of the list

our_list = [1,4,6,3,0,9,18]

def binary_search(a_list, r,x):

   l = len(a_list) - 1 #finishing index
   r = 0 #starting index
   total = 0 

   while r <= l: #while starting index is <= to finishing index
        mid = 1 +  )/ 2

        if a_list(mid) == x:
            return mid, total

        elif a_list[mid] < x:
            r = mid + 1 

        else:
            l = mid - 1 
        total += 1
        
    return -1

