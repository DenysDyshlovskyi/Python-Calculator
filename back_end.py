def leggSammen():
    tall1 = input("Skriv inn det første tallet: ")
    tall2 = input("Skriv inn det andre tallet: ")
    sum = int(tall1) + int(tall2)
    print(f'{tall1} + {tall2} = {sum}')


def trekkFra():
    tall1 = input("Skriv inn det første tallet: ")
    tall2 = input("Skriv inn det andre tallet: ")
    diff = int(tall1) - int(tall2)
    print(f'{tall1} - {tall2} = {diff}')

def gange():
    tall1 = input("Skriv inn det første tallet: ")
    tall2 = input("Skriv inn det andre tallet: ")
    produkt = int(tall1) * int(tall2)
    print(f'{tall1} * {tall2} = {produkt}')
    
def dele():
    tall1 = int(input("Skriv inn det første tallet: "))
    tall2 = int(input("Skriv inn det andre tallet: "))
    if int(tall2) <= 0:
        print("[ERROR] - Kan ikke dele på 0!")
        return
    elif int(tall1) <= 0:
        print("[ERROR] - Kan ikke dele 0 (Eksempel: 0 / 10 = 0)!")
        return
    result = int(tall1) / int(tall2)
    print(f'{tall1} / {tall2} = {result}')
    