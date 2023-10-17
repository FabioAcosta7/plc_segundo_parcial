link de invitavion replit: https://replit.com/join/hfvxjskmua-fabiofornasari

grasa = float(input("Ingrese la cantidad de grasa(gramos):"))
azucar = float(input( "Ingrese la tasa de azucar(gramos):"))
sodio = float(input("Ingrese la cantidad de sodio(miligramos):"))
if grasa <= 5 and azucar <= 10 and sodio <= 100:
  print("Alimento bajo en grasa, azucar y sodio")
elif grasa <= 5 and azucar <= 10:
  print("Alimento bajo en grasa y azucar")
elif sodio <= 100:
  print("Alimento bajo en sodio")
else:
  print("Se deben considerar las advertencias nutricionales")
