import csv
import pandas as pd

file_1 = 'Stars.csv'
file_2 = 'dwarf.csv'
d1 = []
d2 = []

with open(file_1, "r",encoding='utf8') as f:
    csvreader = csv.reader(f)
    for i in csvreader: 
        d1.append(i)

with open(file_2, "r",encoding='utf8') as f:
    csvreader = csv.reader(f)
    for i in csvreader: 
        d2 .append(i)

h1 = d1[0]
p_d1 = d1[1:]
h2 = d2[0]
p_d2 = d2[1:]

h = h1+h2

p_d =[]

for i in p_d1:
    p_d.append(i)
for j in p_d2:
    p_d.append(j)

with open("all_stars.csv", "w", encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(p_d)
    
df = pd.read_csv('all_stars.csv')
df.tail(8)