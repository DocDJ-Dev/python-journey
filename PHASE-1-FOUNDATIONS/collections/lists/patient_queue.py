queue = []

queue.append("Patient A")
queue.append("Patient B")
queue.append("Patient C")

next_seen = queue.pop(0)  # first in, first out

print(next_seen)
print(queue)

# .pop(0) removes from the front
# .pop() removes from the end
# For a long list, popping from the front is slower than popping from the end, because every remaining item has to shift down one position internally.
