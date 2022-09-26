p=0
prajmer=0
a=1
while a != 0:
    c=int(input('Zadaj nejaké číslo: '))
    if c != 0:
        print('Ďakujem, zadaj dalšie ,ak nechceš pokračovať zadaj nulu.')
        p=p+1
        prajmer=prajmer+c
        a=1
    else:
        a=0
        hotovo=prajmer//p
        print(f'Dakujem za spolupracu priemer tvojich čisel je {hotovo}.')

