f = open("Chapter_09 PS/poem.txt")

content = f.read()
if("believe" in content):
    print("believe is present in poem.")
else:
    print("believe is not present in poem.")

f.close()