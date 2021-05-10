import tracemalloc  # importing package to tracing the memory
import time  # importing package to tracing the time
import csv  # importing package to handle the csv file

tracemalloc.start()
start_time = time.time()

french_dict = {}
f1 = open('french_dictionary.csv', 'r')
csv_reader = csv.reader(f1)
for row in csv_reader:
    french_dict[row[0]] = row[1]  # Converting the french_dictionary.csv file in python dictionary
# print(french_dict)

f2 = open('find_words.txt', 'r')
all = f2.read()
find_words_list = all.split()  # Converting the find_words in python list
# print(find_words_list)
f2.close()
# print(type(find_words_list))

result = dict()
with open('shakespeare.txt', 'r') as file:
    filedata = file.read()

# Main part of the program i.e.replacing
f3 = open('t8.shakespeare.txt', 'r')
for line in f3:
    words = line.split()
    for word in words:
        if word.lower() in find_words_list:
            # print(f3.word)
            if word.lower() in result:
                result[word.lower()] += 1
            elif word.lower().strip(",") in result:
                result[word.lower().strip(",")] += 1
            elif word.lower().strip("'s") in result:
                result[word.lower().strip("'s")] += 1
            elif word.lower().strip("-") in result:
                result[word.lower().strip("-")] += 1
            elif word.lower().strip(";") in result:
                result[word.lower().strip(";")] += 1
            elif word.lower().strip(":") in result:
                result[word.lower().strip(":")] += 1
            elif word.lower().strip(".") in result:
                result[word.lower().strip(".")] += 1
            elif word.lower().strip("?") in result:
                result[word.lower().strip("?")] += 1
            elif word.lower().strip(".'") in result:
                result[word.lower().strip(".'")] += 1
            else:
                result[word.lower()] = 1
                filedata = filedata.replace(word, french_dict[word.lower()])
                newword = word + ","
                filedata = filedata.replace(newword, french_dict[word.lower()])
                newword = word + "'s"
                filedata = filedata.replace(newword, french_dict[word.lower()])
                newword = word + ":"
                filedata = filedata.replace(newword, french_dict[word.lower()])
                newword = word + "."
                filedata = filedata.replace(newword, french_dict[word.lower()])
                newword = word + "-"
                filedata = filedata.replace(newword, french_dict[word.lower()])
                newword = word + ";"
                filedata = filedata.replace(newword, french_dict[word.lower()])
                newword = word + "?"
                filedata = filedata.replace(newword, french_dict[word.lower()])
                newword = word + ".'"
                filedata = filedata.replace(newword, french_dict[word.lower()])

# print(result)

with open('t8.shakespeare.translated.txt', 'w') as file:   # Saving the translated t8.shakespeare file
    file.write(filedata)

with open('frequency.csv', 'w', newline='') as csvfile:    # Saving the frequency.csv file
    fieldnames = ['English_word', 'French_word', 'Count']
    thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    thewriter.writeheader()
    for i in result:
        thewriter.writerow({'English_word': i, 'French_word': french_dict[i], 'Count': result[i]})

print("Execution Time: %.2f" % (time.time() - start_time))   # Printing the execution time
print("Memory Usage:", tracemalloc.get_traced_memory())      # Printing the memory usage
tracemalloc.stop()
