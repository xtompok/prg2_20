import random
import time
from test_data import gen_test_data, gen_big_test_data

# vrati minimum ze seznamu
def min(l:list):
    amin = l[0]
    for x in l:
        if amin > x:
            amin = x
    return amin

print(min([1,3,6,3,4,90]))

# vrati True, pokud je prvek v seznamu
# Slozitost O(n)
def in_list(l:list, e):
    for x in l:
        if e == x:
            return True
    return False


# vrati True, pokud je prvek v setridenem seznamu
# funkce je pomala, protoze pri kazdem zanoreni kopiruje prvky seznamu (slice vytvari kopii)
# Slozitost O(n)
def in_sorted_list_slow(l:list, e):
    if l == []:
        return False

    # Prvek v polovine je mensi nez e
    if l[len(l)//2] < e:    # Je potreba pouzit dvojite lomitko, aby slo o celociselne deleni
        return in_sorted_list(l[len(l)//2+1:],e)
    # Prvek v polovine je vetsi nez e
    elif l[len(l)//2] > e:
        return in_sorted_list(l[0:len(l)//2],e)
    # Prvek v polovine je e
    else:
        return True

# Pomocna funkce pro binarni vyhledavani
# Rekurzivne najde minimum ze setrideneho seznamu
# start je index prvniho prvku, ktery do podseznamu patri
# end je index prvniho prvku, ktery do podseznamu nepatri
def in_sorted_list_helper(l:list, start:int, end:int, e):
    # l[start] je prvni z podseznamu
    # l[end-1] je posledni z podseznamu
    if (end - start) == 0:
        return False
    if (end - start) == 1:
        if l[start] == e:
            return True
        else:
            return False
    mid = (start + end)//2
    if l[mid] < e:
        in_sorted_list_helper(l,mid+1,end,e)
    if l[mid] > e:
        in_sorted_list_helper(l,start,mid,e)
    else: # l[mid] == e
        return True

# vrati True, pokud je prvek v setridenem seznamu
# vyhledava pomoci binarniho vyhledavani v O(log n)
def in_sorted_list(l:list, e):
    return in_sorted_list_helper(l,0,len(l),e)



print(gen_test_data(30,sorted=True))
big_data = gen_big_test_data(10_000_000)
elem = random.randint(0,1000)

print("Zacinam merit")
start_time = time.time()
in_sorted_list(big_data,elem)
end_time = time.time()
print("Binarni vyhledavani:",end_time-start_time)

start_time = time.time()
in_list(big_data,elem)
end_time = time.time()
print("Linearni pruchod:", end_time-start_time)

start_time = time.time()
in_sorted_list_slow(big_data,elem)
end_time = time.time()
print("Binarni vyhledavani s kopirovanim:",end_time-start_time)

start_time = time.time()
elem in big_data
end_time = time.time()
print("Pythoni operator 'in':",end_time-start_time)



