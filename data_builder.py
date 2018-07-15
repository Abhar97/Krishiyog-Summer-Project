import csv

def data_builder():
    with open('farmers.csv','r') as file:
        reader = csv.reader(file)

        land = []
        soil = []
        income = []
        rain = []
        iol = []
        Y = []

        for row in reader:
            land.append(float(row[0])/25)
            iol.append(float(row[1])/100)
            soil.append(float(row[2])/10)
            rain.append(float(row[3])/1.5)
            income.append(float(row[4])/100)
            Y.append(row[5])

        file.close()

    X = [[a,b,c,d,e] for a,b,c,d,e in zip(land,iol,soil,rain,income)]

    return X,Y
