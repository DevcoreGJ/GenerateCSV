import random
import csv

# set number of rows to generate
num_rows = 3

# generate random data
data = [(random.randint(5, 7), random.randint(1, 90)) for _ in range(num_rows)]

# save data to csv
with open('study6-7hoursbad.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['studyTime', 'score'])
    for row in data:
        writer.writerow(row)
