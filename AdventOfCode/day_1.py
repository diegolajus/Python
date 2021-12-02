# PART 1

file = open('file_1.txt')

str_list=""
parsed=[]
counter = 0

for line in file.readlines():
    str_list+=str(line)

for e in str_list.split("\n"):
    parsed.append(int(e))

for i in range(1, len(parsed)):
    if parsed[int(i) - 1] < parsed[i]:
        print(f'{parsed[i]} (Decrease)')
        counter = counter + 1
    if parsed[int(i) - 1] > parsed[i]:
        print(f'{parsed[i]} (Increase)')

print (counter)
