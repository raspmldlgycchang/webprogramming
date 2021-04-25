import csv
with open("./public/csvs/1.csv") as csvf:
    #table = [line.split(",") for line in csvf]
    table = [row for row in csv.reader(csvf)]
    print(table)