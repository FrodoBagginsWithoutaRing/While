#napíš program, ktorý bude v cykle načítavať slová dovtedy, pokiaľ nezadáte slovo začínajúce sa
# na písmeno "x". Program vypíše celkový počet znakov všetkých slov okrem posledného slova, začínajúceho sa na x
a=0
l=0
while a != 1:
    c=input('Zadaj nejaké slovo: ')
    c=str.lower(c)
    k=c[0]
    if k != "x":
        b=len(c)
        print(f'Zadaj dalšie.')
        a=0
        l=l+b
    else:
        print(f'Dakujem za spolupracu ale slova na x nemusím takže končíš. Počet písmen vo všetkých tvojích slovach bol {l}.')
        a=1
