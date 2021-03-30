from collections import deque

# Create queue with capacity 30
dq = deque(maxlen=30)

# Append each line to the start of the queue
# If the capacity is exceeded, elements from the end of the queue are discarded
with open("cv05/souradnice.json") as f:
    for line in f:
        dq.appendleft(line)

# Print elements of the queue, in the order that they were added (aka pop from the end)
while len(dq) > 0:
    print(dq.pop(),end="")
