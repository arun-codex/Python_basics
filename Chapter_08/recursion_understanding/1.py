#recursive function (function who call itself)

def show(n):
    if n==0:        # Base case
        return
    print(n)
    show(n-1)
show(6)
