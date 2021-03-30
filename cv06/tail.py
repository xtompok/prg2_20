from collections import deque

dq = deque(maxlen=30)

with open("cv05/souradnice.json") as f:
    for line in f:
        dq.appendleft(line)

while len(dq) > 0:
    print(dq.pop(),end="")
