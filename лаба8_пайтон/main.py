import csv

max = 0.0
min = 100.0
try:
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if row[0] == "Exports of goods and services (% of GDP)":
                if row[len(row)-1] != "..":
                    res = float(row[len(row)-1]) 
                    if res > max:
                        max = float(row[len(row)-1])
                    if res < min:
                        min = float(row[len(row)-1])
                    print(' '.join(row))
except FileNotFoundError:
    print("file not found")
try:
    with open('new_data.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['max ='] + [max] + ['min ='] + [min])
except FileExistsError:
    print("file not exist")
try:
    with open('new_data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(' '.join(row))
except FileNotFoundError:
    print("file not found")


