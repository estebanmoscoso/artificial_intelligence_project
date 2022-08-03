import csv
from os.path import exists
with open('test.csv', 'r') as infile:
    csv_reader = csv.reader(infile, delimiter=',')
    line_count = 0
    with open('experiments/1/test.csv', mode='w') as outfile:
        csv_writer = csv.writer(outfile, delimiter=',')
        row1 = next(csv_reader)
        csv_writer.writerow(row1)
        for row in csv_reader:
            if exists('/Users/sebastianmoscoso/Documents/Dev/Yachay/CheXNet-Keras/data/images/'+row[0]):
                csv_writer.writerow(row)
