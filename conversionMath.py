
#This is Pound - Feet to Newton - meter
def pfToNm():
  #while loop to keep the user in the loop until they enter a valid number
   while True:
     #try for the input
     try:
       pf = float(input("enter a value in pound-feet: "))
     #prevent user from entering anything other than a float
     except ValueError:
       print("Please enter a number")
       continue
     #after entering a number break the loop
     else:
       break
   #equation for newton meters to foot pounds
   nm = pf / .73756
   #rounding the nm variable to 3 places
   nmRound = round(nm, 3)
   #getting your pound feet to inches
   poundInch = pf * 12
   #round pound inch to 3 places
   piRound = round(poundInch, 3)
   #print to console our final calculations
   print(pf, "pound-feet is equal to ", nmRound, "newton-meters and ", piRound, "pound-inches")
   input("press ENTER to continue...")

#This is newton - meter to pound - feet
#This is almost identical to pfToNm() 
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
