T = input("Digite seu post:")
limite = 140

if len (T) <=limite:
  numero = sum (c.isalpha() for c in T)
  letra  = sum (c.isdigit() for c in T)
  print("TWITTER")
  
elif T.isalpha():
  letra = T
  print("TWITTER")
  
else:
    print ("mute")

