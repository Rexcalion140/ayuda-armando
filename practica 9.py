peso=float(input("ingrese su peso en kg: \n"))
altura=float(input("ingrese su altura en m: \n"))

indice=float(peso/altura**2)

if indice<20:
    print("peso bajo")
elif 20<=indice and indice<25:
  print("normal")
elif 25<=indice and indice<30:
   print("sobre peso")
elif 30<=indice and indice<40:
   print("obesidad")
else:
   print("obesidad morvida")