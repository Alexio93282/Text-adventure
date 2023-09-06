

valg1 = input("Du finner en landsby og går inn i et tomt hus. Hva gjør du A: du lar huset være og går ut B: Du raner huset for alt det har ")
        
if valg1 == "A":

        print("Du går ut på gaten og går sør og dør av sult")

if valg1 == "B":
        print("Du finner et bra sverd allerede slipt med en god rustning til å beskytte deg selv, og du finner noen magiske bøker med noen bra magi kastninger.")
    
        print("du går ut av huset og går til kongens slott mot nord")

        print("etter 3 dager er du med kongens slott")

        print("du ser at alle i slotts byen flykter opp til slottet ")

valg2 = input("Du kan enten A: følge med landsbyboerne og spørre hvorfor de flykter B: Ta denne sjansen til å see gjennom husene og ta det du trenger.")

Troll_angrep = input("Du stopper å går tilbake til ingangen til slotts byen og venter på trollene")

if valg2 == "A":

    print("Du går opp til en landsbybeboer som sier de flykter fordi et troll er på vei")
        

if valg2 =="B":
    print("Du ser gjennom alle husene og finner en bunnløs bøtte med sverdet excalibur en deomn rustning og en ciggar")



def start():
    print("Du våkner tied up i en cart som en fange med 3 andre personer")

    print("man: ah you are finally awake")

    print("info: du skal bli halshugget")

    valg = input("Hva gjør du? A: løper bort B: akksepter din sjebne ")

    if valg == "B": 
        Game_over()

    if valg == "A":
        
        print("Det kommer en drage å angriper byen du er i så du klarer å slippe unna suksesfult")


def saved():
     print

def Game_over():
     print("DEAD")
     exit() 

start()