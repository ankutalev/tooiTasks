import csv

new_csv_images = open("3_or_more.csv", 'w')
new_csv_price = open("price.csv", 'w')
new_csv_columns = open("columns.csv", 'w')

writer1 = csv.writer(new_csv_images, delimiter=',')
writer2 = csv.writer(new_csv_price, delimiter=',')
writer3 = csv.writer(new_csv_columns, delimiter=',')

with open('stage3_test.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in spamreader:
        if len((row[1]).split(',')) > 3 or i == 0:
            writer1.writerow(row)
        if i == 0 or 10000 < float(row[4]) <= 50000:
            row[0],row[4] = row[4],row[0]
            writer2.writerow(row)
        del row[1], row[2]
        writer3.writerow(row)
        i = 1

new_csv_columns.close()
new_csv_images.close()
new_csv_price.close()
