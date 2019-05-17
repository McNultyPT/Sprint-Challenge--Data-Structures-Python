import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# under a second
# duplicates = [name for name in names_1 if name in names_2]

duplicates = []
dict_1 = {}
dict_2 = {}

for name in names_1:
    dict_1[name] = name

for name in names_2:
    dict_2[name] = name

for name in dict_1.keys():
    if dict_2.get(name):
        duplicates.append(dict_1.get(name))
    
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

