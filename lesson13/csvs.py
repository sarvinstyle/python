import csv

# with open("lesson13\\docs\\data.csv" , "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["id" , "name" , "salary"])
#     writer.writerow([1 , "sarvin" , 100])
#     writer.writerow([2 , "sara" , 110])


with open("lesson13\\docs\\data.csv" ) as file:
    reader = csv.reader(file) 
    for row in reader :
        print(row)