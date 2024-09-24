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
        print("[ERROR] - Kan ikke dele på ", tall2, "!")
        return
    elif int(tall1) <= 0:
        print("[ERROR] - Kan ikke dele", tall1, "(Eksempel: 0 / ", tall2, " = 0)!")
        return
    result = int(tall1) / int(tall2)
    print(f'{tall1} / {tall2} = {result}')
    
def snitt():
    total = 0
    amount = int(input("Hvor mange tall vil du ha gjennomsnitt av? "))
    for i in range(amount):
        userinput = int(input(f"Skriv inn tall nummer {i+1}: "))
        total = total + userinput
    snitt = total / amount
    print(snitt)
    
    