import os
import csv
import datetime

path_files = "files"
path_arch = os.path.join(os.getcwd(), path_files)
logs = 'BBB_nuevo.csv'

with open(os.path.join(path_arch, logs)) as logs_moodle:
    data_logs = csv.reader(logs_moodle, delimiter=',')
    header, logs_recurso = next(data_logs), list(data_logs)

dias_semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
#formato = "%d/%m/%Y , %H:%M:%S"
#print(datetime.datetime.strptime(linea[0], formato).weekday())

dias = []

for linea in logs_recurso:
    #print(linea[0])
    nro = datetime.datetime.strptime(linea[0], "%d/%m/%Y %H:%M").weekday()
    dias.append(dias_semana[nro])
    #print(dias_semana[nro])

#insiso 4
#print(dias)
aux = max(set(dias), key=dias.count)
print(f"El dia de la semana con mas registros es {aux}")

#insiso 5
max_date = datetime.datetime.min
min_date = datetime.datetime.max

for linea in logs_recurso:
    this_date = datetime.datetime.strptime(linea[0], "%d/%m/%Y %H:%M")
    if this_date < min_date:
        min_date = this_date
    if this_date > max_date:
        max_date = this_date
    #dias.append(dias_semana[nro])
    #print(dias_semana[nro])

print(f"min: {min_date}, max: {max_date}")
print(f"La cantidad de dias que pasaron entre el primer registro  el ultimo es de: {max_date - min_date}")