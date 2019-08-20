def simple_search(a_list,item):
    total = 0
    for i in a_list:
        total += 1
        if i == item:
            return item, total
    return False

our_list = [1,4,6,3,0,9,18]

print(simple_search(our_list,18))

#best case is O(1)
#worst case is O(n)