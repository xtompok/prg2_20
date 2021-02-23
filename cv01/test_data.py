import random

def gen_test_data(n:int, sorted=False):
    letters = [chr(i) for i in range(ord('a'),ord('z'))]+[chr(i) for i in range(ord('A'),ord('Z'))]
    test_data = random.sample(letters,n)
    if sorted:
        test_data.sort()
    return test_data

def gen_big_test_data(n:int, amin=0, amax=1000):
    return sorted([random.randint(amin,amax) for _ in range(n)])
