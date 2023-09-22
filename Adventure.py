hp = 100
excalibur = 0 
demon_rustning = 0
cigar = 0
dårlig_sverd = 0
sverd = 0 
rustning = 0
ringbrynje = 0
magibok = 0
gull = 0
healing = 0

hoarde_visited = False

import random


def start():
    print("Du våkner tied up i en cart som en fange med 3 andre personer")

    print("man: ah you are finally awake")

    print("info: du skal bli halshugget")

    valg = input("Hva gjør du? A: løper bort B: akksepter din sjebne ")

    if valg == "B": 
        Game_over()

    elif valg == "A":
        print()
        print()
        print("Det kommer en drage å angriper byen du er i så du klarer å slippe unna suksesfult")
    saved()


def saved():
    print("du går mot nord for å prøve å få hjelp av kongen")
    
    valg1 = input("Du finner en landsby og går inn i et tomt hus. Hva gjør du A: du lar huset være og går ut B: Du raner huset for alt det har ")
        
    if valg1 == "A":
        print()
        print()
        print("Du går til et annet hus")
        hus2()
        

    elif valg1 == "B":
        global rustning, hoarde_visited,gull
        global dårlig_sverd
        global magibok
        
        print()
        print()
        print("Du finner et medioker sverd som er halv slipt med en litt under gjennomsnitlig rustning til å beskytte deg selv, og du finner noen magiske bøker med noen ukjente magi kastninger og en pose med 9 gullmynter.")
        rustning += 1 
        dårlig_sverd += 1
        magibok += 1
        gull += 9
        
    
        print("du går ut av huset og går til kongens slott mot nord")

        print("etter 3 dager er du med kongens slott")

        print("du ser at alle i slotts byen flykter opp til slottet")
    horde()

def hus2():
    global gull, sverd, ringbrynje, healing, hoarde_visited

    print("i det andre huset finner du noe mat og et sverd du går i nedre etasjen og finner en skjorte laget av ringbrynje og en pose med 9 gull, du går ut av huset og begyner å gå mot sør\n")
    gull += 9
    ringbrynje += 1
    sverd += 1
    healing += 3


    valg_mot_sør = input("Etter du har gått et stykke finner du en splittet vei met to skilt. Du kan A gå til venstre B gå til høyre eller C gå tilbake og prøve å finne kongens slott.\n")
    if hoarde_visited == False:
            hoarde_visited = True

    if valg_mot_sør == "A":
        print("Du ser på skiltet til venstre og ser at det sier hoggsmed landsby og du husker at du kan få bedre våpen og rustning der.\n")
        venstre()

    elif valg_mot_sør == "B":
        print("Du ser på skiltet til høyre og ser at det sier nowhere du har hørt rukter om at det er en veldig god pub der.")
        høyre()

    elif valg_mot_sør == "C":
        print("du bestemmer deg for å få tilbake til den forige landsbyen og fortsette nord.")
        print()
        print()
        print("etter 3 dager er du med kongens slott")
        print("du ser at alle i slotts byen flykter opp til slottet")
        horde()
        
def venstre():
    global gull
    print("Du kommer til hoggsmed drar til nermeste smed og spør om du kan få sverdet ditt oppgradert")

    valg_oppgradering = input("Smeen spør hva du betaler med du kan A gi han 3 gull for sverdet eller B gjøre et magi triks ")

    if valg_oppgradering == "A":
        gull -= 3
        print(f"du har nå {gull} gull igjen")
        print("Du betaler med gull og smeen er fornøyd så du går til en bar og drikker litt")
        i_baren()
    elif valg_oppgradering == "B":
        print("Smeen aksepterer ikke magi triks og roper på polti")
        start()


def i_baren():
    global gull

    print("Du kommer in i baren og bestiller en drink")
    gull -= 1
    print("Du sitter der etter å ha tatt 2 drinker til og bestemer deg for å drar\n")
    gull -= 2
    
    print(f"du har nå {gull} gull igjen\n")
    print("etter du har reist deg føler du noe hardt i hodet og alt blir svart")
    print("De tok alt")
    gull -= 4
    start() 

    
def høyre():
    print("Du er nå kommet til nowhere og ser etter puben du har hørt så mye om\n")
    print("Du finner ikke puben men du ser en nydelig dame som sitter alene på en resturant\n")
    print("Du går til henne og spør henne om du kan sitte, hun sier ja\n")
    print("Du spørr henne om du kan ta henne med på en date senere den dagen\n")
    rizz = random.randint (0,10)
    print(f"Dit rizz roll er {rizz}\n")
    if rizz <= 5:
        print("Hun syntes du er en creep og roper på politiet\n")
        start()
    if rizz >= 5:
        print("Hun sier ja, tiden går og dere er gift med 2 barn og et lykkelig liv\n")
        happy_end()


def happy_end():
    exit()



def horde():
    global excalibur, cigar, demon_rustning,rustning, dårlig_sverd, magibok, hoarde_visited, hp, healing
    
    valg2 = input("Du kan enten A: Se litt igjennom husene før du bestemmer deg å følge med en av landsbyboerne og spørre hvorfor de flykter Eller B: Dra ut av slottsbyen.")
    
    

    if valg2 == "A":
        if hoarde_visited == False:
            hoarde_visited = True
            print()
            print()
            print("Du ser gjennom alle husene og finner en bunnløs bøtte med sverdet excalibur en demon rustning og en ciggar, etter det Du går opp til en landsbybeboer og spør hva som skjer den sier at de flykter fordi et troll er på vei")

            excalibur +=1
            cigar += 1
            demon_rustning += 1 
            rustning -= 1
            dårlig_sverd -= 1

            troll_tall = random.randint (75, 200)
            
            print("+ excalibur, cigar, demon rustning\n")
            print("-rustning, -dårlig sverd\n")
            
            input("Du stopper å går tilbake til ingangen til slotts byen og venter på trollene       trykk en knapp")
        
            print(f"Du står med porten i 10 minutter før det kommer {troll_tall} troll foran deg")
            fight_or_flight()
        
        else:
            print("De sier at de flykter fra troll\n")
            print("")

        troll_hp = 100
        fighting = True
        while fighting:
            print(f"Du har {hp} hp")
            print(f"trollene har {troll_hp} hp")
            print(f"Du har {healing} potioner")

           
            valg = input("A: Hit B: heal")
            
            if valg == "A":
                dmg = random.randint(1,10)
                troll_hp -= dmg
                print(f"Trollene tok {dmg} skade\n")
            
            elif valg == "B":
                if healing >0:
                    healing -=1
                    heal = random.randint(10,15)
                    hp += heal
                    print(f"Du fikk {heal} hp")
                else: 
                    print("Du har ikke mer healing")
            
            if troll_hp < 0:
                print("Trollene er døde\n")
                krisen_er_over()
                
            else:
                if valg != "B":
                    Troll_dmg = random.randint(5,10)
                    hp -= Troll_dmg
                    print(f"Du mistet {Troll_dmg} hp")
                    if hp < 1:
                        print("You failed")
                        exit()
                
            


        

    elif valg2 =="B":
        print("Du går ut igjennom porten, der står det en troll horde som tramper deg ned")
        Game_over()

    

def fight_or_flight():
    global hp
    print()
    print()

    random_min = random.randint(1,7)
    pain = random.randint (1,5)
    
    valg3 = input("Du kan a ombestemme deg og løpe opp til slotte med resten av landsbybeboerne, eller B sloss med trollene")
    
    if valg3 == "A":
        print("Du klarer å flykte til slottet på grunn av den bra rustningen din.")
        du_flykter()

    elif valg3 =="B":
        print(f"Du dreper alle trollene på {random_min} minutter og løper opp til slotte for å si at krisen er over.")
        hp -= pain
        print(f"du mister {pain} hp")
        print("du har", hp, "hp igjen")
        krisen_er_over()

    

def du_flykter():
    print("Du kommer deg til slottet og sier til alle i det at det ikke er trykt de må flykte ut av byen og at du kommer til å beskytte dem mens de flykter til en annen by.")
    iden_andre_byen()

def iden_andre_byen():
    print("Beboerene er sjokkert over at kongen er i byen deres\n")
    print("Kongen vil gjøre deg om til ridder, du må akseptere")

    ridder_eller_gift = input("Du kan A: holde deg til dine ridderlige oppgaver og være loyal mot kongen eller B: Gifte deg med prinsessen om noen år når hun er 18")

    if ridder_eller_gift == "A":
        print("Du holder deg til dine ridderlige oppgaver og beskytter kongen igjennom hele livet ditt.")
    
    elif ridder_eller_gift == "B":
        print("Du gifter deg med prinsessen, du blir konge og du og din kone lever lykkelige resten av livet.")

def krisen_er_over():
    print()
    print()
    print("Du kommer inn i slottet og sier at trollene er bekjempet og at byen er trygg.")

    valg4 = input("Beboerene av slottsbyen takker deg og spør om du kan bli litt mens de holder en bankett for å feire at du reddet dem du kan: A takke ja og bli med på banketten før du snakker med kongen eller B du sier nei og at du må snakke med kongen med en gang.")
    
    if valg4 == "A":
        print("Du spiser en veldig god middag og spør når du er ferdig om du kan snakke med kongen de sier ja og du blir tatt in i troneromet.")
        i_tronerommet()
        
    
    elif valg4 == "B":
        print("De blir sure men tar deg med til troneromet likevel")
        i_tronerommet()


def i_tronerommet():
    print()
    print()

    valg5 = input("Du er i tronerommet: Du har valget om A: være høffelig og prate med kongen på en sivilisert måte eller B: Si det du tenker på uten noe tanke på høfflighet")

    if valg5 == "A":
        print("Dere prater på¨en ordentlig måte og kommer til en konklusjon om at du kan gifte deg med datteren hans når hun er 18.")
        print("du er 16 btw")
        glad_slutt()

    elif valg5 == "B":
        print("Kongen liker ikke den harsje tonen din og får en av vaktene til å slå deg ut.")
        dårlig_slutt()

def glad_slutt():
    print("Det går 3 år og du gifter deg med prinsessen og lever et bra liv.")
    exit()

def dårlig_slutt():
    global excalibur, cigar, demon_rustning, magibok
    print("De robber deg for alt du har og sender deg til å bli hals hogget.")
    excalibur -=1
    cigar -= 1
    demon_rustning -= 1 
    magibok -= 1
    start()


def Game_over():
     print("DEAD")
     exit() 

start()

