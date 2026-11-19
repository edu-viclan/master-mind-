# nu sk det finns ett master mind spel. där det ska finnas 2 olika lägen ett svårtare, lätt
# det svåra ska kunna ha ex 6691 
# det lätta ska inte kunn ha samm av 2 siftror ex: ej (6691) utan 6712 ( har inte 2 av samma)
import random 
#✔️✅✔☐


# funktionen som väljer svårighets grad. 1(enkel) eller 2(svår) 
def inmat(txt):
       while True:
               try:
                    if int(input(txt)) <2:
                          print("ogiltigt värl 1 eller 2")
                          continue
                    elif int(input(txt)) == 1:
                          return "1"
                    elif int(input(txt)) == 2:
                          return "2"
               except ValueError:
                   print("ogiltigt")



print(inmat("vilken svårighets grad vill du ha "))




                   

