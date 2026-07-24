# Write a python function to remove a given word from a list and strip it at the same time.

def rem(l, word):
    for item in l:
        return l.remove(word)

l = ["Arun", "Rohan"]

print(rem(l,"Rohan"))