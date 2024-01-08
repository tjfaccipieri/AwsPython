#usar libs externas para a leitura sequencial de um arquivo CSV
import csv
import copy

#criando um dict para o veiculo
myVehicle = {
  "vin" : "<empty>",
  "make" : "<empty>" ,
  "model" : "<empty>" ,
  "year" : 0,
  "range" : 0,
  "topSpeed" : 0,
  "zeroSixty" : 0.0,
  "mileage" : 0
}

#imprimindo o docionario acima
# for key, value in myVehicle.items():
#   print("{} : {}".format(key,value))

#criando uma lista vazia para guardar os dados do CSV
myInventoryList = []

with open('exercicio6/car_sheet.csv') as csvFile:
  csvReader = csv.reader(csvFile, delimiter=',')
  lineCount = 0
  for row in csvReader:
    if lineCount == 0:
      print(f'column names are: {", ".join(row)}')
      lineCount += 1
    else:
      print(f'vin: {row[0]}, make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
      currentVehicle = copy.deepcopy(myVehicle)
      currentVehicle["vin"] = row[0]
      currentVehicle["make"] = row[1]
      currentVehicle["model"] = row[2]
      currentVehicle["year"] = row[3]
      currentVehicle["range"] = row[4]
      currentVehicle["topSpeed"] = row[5]
      currentVehicle["zeroSixty"] = row[6]
      currentVehicle["mileage"] = row[7]
      myInventoryList.append(currentVehicle)
      lineCount =+ 1
  print(f'Processed {lineCount} lines')

for myCarProperties in myInventoryList:
  for key, value in myCarProperties.items():
    print("{} : {}".format(key, value))
    print("--------")