# Napište bubble sort

def bubble_sort(l:list):
    """ Sorts given list in place using bubble sort.
        Does not return anything"""
    for i in range(len(l)-1,0,-1):
        for j in range(0,i):
            if l[j]>l[j+1]:
                tmp = l[j]
                l[j] = l[j+1]
                l[j+1] = tmp


if __name__ == "__main__":
    l = [6,4,5,2,6,78,1]
    bubble_sort(l)
    print(l)


