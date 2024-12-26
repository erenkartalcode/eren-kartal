konto=float(1000)
while True:
  menu=int(input("1 Einzahlen 2 Auszahlen"))
  geld=None
  if menu==1:
    geld=float(input("Wie viel zahlen Geld ein?"))
    if geld<0:
      print("Negative kontostand!")
      continue
    elif geld>0:  
      konto=konto+geld
      print("Neue Konto: "+ str(konto) + " Karte entnehmen")
      break
  if menu==2:
    geld=float(input("Wie viel zahlen Geld aus?"))
    if geld>konto:
      print("Negative kontostand!")
      continue
    elif 0<=geld<=konto: 
     konto=konto-geld
     print("Neue Konto: "+ str(konto) + " Karte entnehmen")
     break
    elif geld<0:
      print("Ungültige eingabe!")
  else:
   print("Ungültige Auswahl!")
   continue
print("ende")