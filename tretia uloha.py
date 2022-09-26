c= 'nieco'
a=0
while a != 1:
    c=input('Zadaj nejaké meno: ')
    c=str.lower(c)
    if c != "koniec":
        b=len(c)
        print(f'Toto meno ma {b} pismen. Prosím zadaj dalšie meno pre ukončenie zadaj koniec.')
        a=0
    else:
        print('Dakujem za spolupracu.')
        a=1
