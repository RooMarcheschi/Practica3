import datetime 
#El módulo datetime crea un objeto con el cual podemos realizar operaciones para cálculo de fechas.

x = datetime.datetime.now()
print(x)

nro_dia_semana = datetime.datetime.today().weekday()
print(nro_dia_semana)

dias_semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
print(dias_semana[nro_dia_semana])

print(x.hour)

horario_juego = datetime.datetime.now().strftime("%d/%m/%Y , %H:%M:%S")
print(horario_juego)

