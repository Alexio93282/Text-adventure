hp = 100

def rom_1():
    print("du er nå i en fange vogn på vei mot galgen for å bli hengt")
    valg = input("Velg A for rom 2, velg B for rom 3 ")
    if valg == "A":
        rom_2()
    if valg == "B":
        rom_3()

def rom_2():
    print("Du er nå i et fange rom før du blir hengt")
    valg1 = input("Du har en sjanse til å unslippe fengselet, A du unslipper og drar ut på landet for å komme deg unna vaktene B Du velger å ikke dra og venter din skjebene ")
    if valg1 == "A":
     print("Du går i noen timer og finner en forlatt by")
    
    if valg1 == "B":
     rom_3()


def rom_3():
    global hp
    print("Du er nå med galgen og blir hengt")
    hp -= 100
    
    if hp <= 0:
        game_over()


def game_over():
   print("You died")
   exit()

rom_1()