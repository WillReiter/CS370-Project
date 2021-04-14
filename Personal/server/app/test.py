file1 = open("info.txt","r")
list = []
for x in file1:
    list.append(x + '\n')
print(file1.read)