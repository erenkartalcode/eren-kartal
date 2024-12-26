note=int(input("Bitte geben Sie siene Abschlussnote ab!"))
erfah=int(input("Bitte geben Sie seine Programmiererfahrung von 1 bis 5 ab!"))
if note>=90:
 print("Einstellen")
elif note>=70 and erfah==5:
 print("Einstellen")
elif note>=70:
  print("Gespraech eingeladen")
elif erfah==4:
  print("Gespraech eingeladen")
else:
  print("Ablehnen")