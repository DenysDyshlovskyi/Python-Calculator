from back_end import *


def printMeny():
    print("------------------- Kalkulator -------------------")
    print("| 1. Legg sammen                                 |")
    print("| 2. Trekk fra                                   |")
    print("| 3. Gange                                       |")
    print("| 4. Dele                                        |")
    print("| 5. Regn ut gjennomsnitt                        |")
    print("| 6. Avslutt                                     |")
    print("--------------------------------------------------")
    menyvalg = input("Velg operasjon fra menyen: ")
    utfoerMenyvalg(menyvalg)


def utfoerMenyvalg(valgtTall):
    if valgtTall == "1":
        leggSammen()
        pause_og_fortsett()
    elif valgtTall == "2":
        trekkFra()
        pause_og_fortsett()
    elif valgtTall == "3":
        gange()
        pause_og_fortsett()
    elif valgtTall == "4":
        dele()
        pause_og_fortsett()
    elif valgtTall == "5":
        snitt()
        pause_og_fortsett()
    elif valgtTall == "6":
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N ")
        if (bekreftelse == "J" or bekreftelse == "j"):
            exit()
        else:
            printMeny()
    else:
        print("Ugyldig valg. Velg et tall fra 1-6. Trykk en tast for å fortsette")
        printMeny()
    

def pause_og_fortsett():
    input("-- Trykk en tast for å fortsette --")
    printMeny()


printMeny()

