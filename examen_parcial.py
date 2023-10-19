temperatura = int(input("Ingrese la temperatura de la bebida (Celsius):"))
if temperatura < 50:
  print("Debe esperar a que se caliente la bebida")
elif temperatura >= 50 and temperatura <= 70:
  print("Se puede servir de inmediato")
elif temperatura > 70:
  print("Bebida muy caliente, debe esperar a que se enfrie")

hora = int(input("Ingrese la hora del día (horario 24 horas):"))
if hora >= 6 and hora <= 11:
  print("Las bebidas calientes se sirven más rápido")
else:
  print("Esperar el turno")
