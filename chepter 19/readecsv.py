from csv import reader
with open('file.csv', 'r') as f:
   csv_redered = reader(f)
   print(csv_redered)