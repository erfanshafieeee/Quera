# WRITE YOUR CODE HERE
print(' '.join(list(reversed(sorted(list(map(lambda x:x if (ord(x) - 97) % 2 == 0 else x.upper(),input())))))))
