f = open("Chapter_09/file.txt")

# lines = f.readlines()
# print(lines, type(lines))

# line1 = f.readline()
# print(line1, type(line1))

line = f.readline()
while line != "":
    print(line)
    line = f.readline()

f.close()
