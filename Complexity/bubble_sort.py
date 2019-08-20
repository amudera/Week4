our_list = [1,4,6,3,0,9,18]

def bubble_sort(a_list):
    n = len(a_list)
    total = 0

    for i in range(n):

        for j in range(0,n-i-1):

            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
                total += 1 #number of iterations
    return a_list, total

print(bubble_sort(our_list))

#O(n^n)