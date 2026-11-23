# nu sk det finns ett master mind spel. där det ska finnas 2 olika lägen ett svårtare, lätt
# det svåra ska kunna ha ex 6691 
# det lätta ska inte kunn ha samm av 2 siftror ex: ej (6691) utan 6712 ( har inte 2 av samma)
import random 
#✔️✅✔☐


# funktionen som väljer svårighets grad. 1(enkel) eller 2(svår) 
def inmat_LeS(txt):
      while True:
               try:
                    x = int(input(txt))
                    if x > 2:
                        print("ogiltigt välj 1 eller 2")
                        continue
                    elif x == 1:
                          return "1"
                    elif x == 2:
                          return "2"
               except ValueError:
                   print("ogiltigt")
'''
Denna funktion står för säker inmatning av val för svårihetsgrad
'''
def inmat(txt):
    while True:
        x = input(txt)
        if  len(x) != 4 or not x.isdigit():
            print("ogiltigt")
            continue
        else:
            return x
'''
denn funtion är säker inmatning för gissningar ^^^^^^^. 
'''
def num_svår(): 
    lst_ut = []
    for i in range(0,4):
        lst_ut.append(random.randint(1,6))
    return lst_ut
'''
denna funktion slumpar fram talen till den svåra listan
'''
def num_enkel(): # leornado gjorde funktioenn :D   yay 
      #alt ska köras 4 gånger. 
    möjliga_tal = [1,2,3,4,5,6]
    fack_tal = []
    for i in range(0,4):
        random.randint(1,len(möjliga_tal))
        # jag har nu plockat ut ett tal från listan 
        fack_tal.append(möjliga_tal.pop(random.randint(1,(len(möjliga_tal)-1))))
      #jag behöver ja poulationen av listan 
    return fack_tal
'''
denna funktion slumpar fram talen till den enkla listan
'''





# UI building.  shisse
# kontrol
print(inmat("skriv din gissning"))   # ska kolla gissnignen)
# nu har vi fått fram ett rätt svar och ska gämför den med rätt lista från svår relle lätt 
ex= 1256
ex2 = 1234
lol = "lol"
print(f"drag# {"Drag":>9}  {"Feedback":>18}\n {"-"*35} ")
for i in range (12,0,-1):
    
    # men bara på plats 1 vill jag skriva. 
    print (f"{i:>3}#    {ex}                    \n")

 
