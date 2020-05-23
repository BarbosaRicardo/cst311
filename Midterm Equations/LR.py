# This program calculates the transmission time 

import math

#determines the unit and prompts for value
while True:
      valL = int(input('Enter packet size L: '))
      askL = input('Enter unit of packet size L(MB or KB): ')

      valR = int(input('Enter rate R: '))
      askR = input('Enter unit of rate R(Kbps or Mbps): ')
      
      if (askL == 'KB'):
         LK= valL*1024*8
         L = LK
      elif(askL == 'MB'): 
         LM = valL*1024*1024*8
         L = LM

      if(askR =='Mbps'):
         Rm = valR*(10**6)
         R = Rm
      elif(askR=='Kbps'):
         Rk = valR*(10**3)
         R = Rk

      print("Transmission Delay: ", L/R, "seconds")
      print()
      
      cont = input("Continue (Y or N)?: ")
      if(cont.lower() == 'y'):
         continue
      else:
         break
