#This is Pound - Feet to Newton - meter
def pfToNm():
   while True:
     try:
       pf = float(input("enter a value in pound-feet: "))
     except ValueError:
       print("Please enter a number")
       continue
     else:
       break
   nm = pf / .73756
   nmRound = round(nm, 3)
   poundInch = pf * 12
   piRound = round(poundInch, 3)
   print(pf, "pound-feet is equal to ", nmRound, "newton-meters and ", piRound, "pound-inches")
   input("press ENTER to continue...")

#This is newton - meter to pound - feet
def nmToPf():
    while True:
      try:
        nm = float(input("enter a value in Newton-meters: "))
      except ValueError:
        print ("Please enter a number")
        continue
      else:
        break
    pf = nm * .73756
    pfRound = round(pf, 3)
    poundInch = pf * 12
    piRound = round(poundInch, 3)
    print(nm, "newton-meters is equal to ", pfRound, "pound-feet and ", piRound, "pound-inches")
    input("press ENTER to continue...")


  
