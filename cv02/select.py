# Napište select sort
def fce(a:int):
    return -a

print(fce(3))
moje_fce = fce
print(type(moje_fce))
print(moje_fce(4))

def select_sort(l:list, key=None):
    """ Sorts given list in place using select sort.
    Does not return anything"""

    if key == None:
        key = lambda x:x

    # Toto udělám tolikrát, jak dlouhý mám seznam
    for i in range(len(l)):
        amin = key(l[i])
        minidx = i
        # Ve vnitrnim cyklu najdu minimum ze zbývajícího seznamu
        for j in range(i,len(l)):
            if amin > key(l[j]):
                amin = key(l[j])
                minidx = j
            
        # Prohodím ho s prvním zatím nesetříděným prvkem
        tmp = l[minidx]
        l[minidx] = l[i]
        l[i] = tmp

if __name__ == "__main__":
    l = [5,2,3,87,3,5,8,125]
    select_sort(l)
    print(l)
    select_sort(l, key=fce)
    print(l)