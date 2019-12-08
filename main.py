import sys
import conversionMath

pfToNm = conversionMath.pfToNm
nmToPf = conversionMath.nmToPf
clear = "\n" * 100

while True:
 print(clear)
#This is a tool to convert torque values from pound-feet to newton-meters
 
#Main Menu
 print("Torque Wrench Converter")
 print("Written in Python")
 print("By Adrian Edelen")
 print("Please select an option below")
 print("1. Convert From Pound-Feet to Newton-Meters")
 print("2. Convert From Newton-Meters to Pound-Feet")
 print("3. Manual")
 print("4. Exit")
#Grabbing the user's choice
 userSelection = 0
 def userSelect():
     global userSelection
     while True:
       try:
         userSelection = int(input("Select a choice: "))
       except ValueError:
         print("Please enter a number 1-4")
         continue  
       if userSelection > 4 or userSelection < 1:
         print("Please enter a number 1-4")
         continue
       else:
         break
 
 
     
 userSelect()
 
 def userCoices():
   if userSelection == 1:
     pfToNm()
   if userSelection == 2:
     nmToPf()
   if userSelection == 3:
     print("Hey ya dummy, if ya need a manual for this then you might want to take a deep breath, look in the mirror, and rethink your life.")
     input("press ENTER to continue...")
   if userSelection == 4:
     sys.exit()
   if userSelection == 69 or userSelection == 420:
     print("Nice")
 userCoices()
                    
 
 
 
 

