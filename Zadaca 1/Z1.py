#Rock Paper Scissors Lizard Spock u Big Bang Theory stilu

Naziv1 = input("Unesi naziv igrača1:")
Naziv2 = input("Unesi naziv igrača2:")

ponovno = "Da" 
kriva_vrijednost = False

Bodovi1 = int(0)
Bodovi2 = int(0)

#Glavna petlja
while ponovno == "Da":
    print("=" * 20)
    print("Odaberi: Papir, Škare, Kamen, Gušter, Spock")
    print("=" * 20)
    print("PAZI na velika i mala slova prilikom odabira!")

#Odabir
    odabir1 = str(input("{}:".format(Naziv1)))
    odabir2 = str(input("{}:".format(Naziv2)))

#Provjera
    if(odabir1 == odabir2):
        print("Izjednačeno!")
        kriva_vrijednost = True

    elif(odabir1 == "Papir"):
        if(odabir2 == "Kamen"):
            print("{} je pobijedio!".format(Naziv1))
            Bodovi1 += 1 
        elif(odabir2 == "Škare"):
            print("{} je pobijedio!".format(Naziv2))
            Bodovi2 += 1
        elif(odabir2 == "Gušter"):
            print("{} je pobjedio!".format(Naziv2))
            Bodovi2 += 1
        elif(odabir2 == "Spock"):
            print("{} je pobjedio!".format(Naziv1))
            Bodovi1 += 1
        else:
            print("{}, unesena je kriva vrijednost.".format(Naziv2))
            kriva_vrijednost = True

    elif(odabir1 == "Kamen"):
        if(odabir1 == "Škare"):
            print("{} je pobijedio!".format(Naziv1))
            Bodovi1 += 1   
        elif(odabir2 == "Papir"):
            print("{} je pobijedio!".format(Naziv2))
            Bodovi2 += 1
        elif(odabir2 == "Gušter"):
            print("{} je pobjedio!".format(Naziv2))
            Bodovi2 += 1
        elif(odabir2 == "Spock"):
            print("{} je pobjedio!".format(Naziv1))
            Bodovi1 += 1
        else:
            print("{}, unesena je kriva vrijednost..".format(Naziv2))
            kriva_vrijednost = True

    elif(odabir1 == "Škare"):
        if(odabir2 == "Papir"):
            print("{} je pobijedio!".format(Naziv1))
            Bodovi1 += 1   
        elif(odabir2 == "Kamen"):
            print("{} je pobijedio!".format(Naziv2))
            Bodovi2 += 1
        elif(odabir2 == "Gušter"):
            print("{} je pobjedio!".format(Naziv1))
            Bodovi1 += 1
        elif(odabir2 == "Spock"):
            print("{} je pobjedio!".format(Naziv2))
            Bodovi2 += 1   
        else:
            print("{}, unesena je kriva vrijednost.".format(Naziv2))
            kriva_vrijednost = True

    elif(odabir1 == "Gušter"):
        if(odabir2 == "Papir"):
            print("{} je pobijedio!".format(Naziv1))
            Bodovi1 += 1   
        elif(odabir2 == "Kamen"):
            print("{} je pobijedio!".format(Naziv2))
            Bodovi2 += 1
        elif(odabir2 == "Škare"):
            print("{} je pobjedio!".format(Naziv2))
            Bodovi2 += 1
        elif(odabir2 == "Spock"):
            print("{} je pobjedio!".format(Naziv1))
            Bodovi1 += 1   
        else:
            print("{}, unesena je kriva vrijednost.".format(Naziv2))
            kriva_vrijednost = True
    
    elif(odabir1 == "Spock"):
        if(odabir2 == "Papir"):
            print("{} je pobijedio!".format(Naziv2))
            Bodovi2 += 1   
        elif(odabir2 == "Kamen"):
            print("{} je pobijedio!".format(Naziv1))
            Bodovi1 += 1
        elif(odabir2 == "Škare"):
            print("{} je pobjedio!".format(Naziv1))
            Bodovi1 += 1
        elif(odabir2 == "Gušter"):
            print("{} je pobjedio!".format(Naziv2))
            Bodovi2 += 1
        else:
            print("{}, unesena je kriva vrijednost.".format(Naziv2))
            kriva_vrijednost = True

    else:
        print("{}, unesena je kriva vrijednost.".format(Naziv1))
        kriva_vrijednost = True

    #Bodovi se ne prikazuju ako je unesena kriva vrijednost ili je izjednačeno
    if(kriva_vrijednost == False):
        print("=" * 20)
        print("{} ima {} bodova".format(Naziv1, Bodovi1))
        print("{} ima {} bodova".format(Naziv2, Bodovi2))
        print("=" * 20)

    ponovno = input("Želite li igrati ponovno? (Da/Ne)")
