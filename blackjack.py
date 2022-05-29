import random

talia = []
g = 0
p = 'a'
gracz1 = 0
gracz2 = 0
gracz3 = 0
gracz4 = 0
gracze = [gracz1, gracz2, gracz3, gracz4]
czy_pc = ['gracz', 'gracz', 'gracz', 'komputer']
decyzja = ['t', 't', 't', 't']

g = int(input("Ile graczy bedzie uczestniczylo w grze? "))
while g < 2 or g > 3:
    print("Podaj prawidlowa ilosc graczy")
    g = int(input("Ile graczy bedzie uczestniczylo w grze? "))

q = int(input("Ile graczy ma zastapic komputer? "))
while q < 0 or q > 3:
    print("Podaj prawidlowa ilosc graczy")
    q = int(input("Ile graczy ma zastapic komputer? "))

for i in range(q):
    czy_pc[i] = 'komputer'

wynik = [[gracze[0], 'Gracz nr 1', czy_pc[0], decyzja[0]],
         [gracze[1], 'Gracz nr 2', czy_pc[1], decyzja[1]],
         [gracze[2], 'Gracz nr 3', czy_pc[2], decyzja[2]],
         [gracze[3], 'Komputer', czy_pc[3], decyzja[3]]]

x = 1
for i in range(2, 11):
    for j in range(4):
        talia.append(1 + x)
    x += 1

#Po 3 figury
for i in range(3):
    for j in range(4):
        talia.append(10)
#4 asy
for j in range(4):
    talia.append(11)

gierka = 1


n = len(talia)
for i in range(g):
    e = random.randint(0, n - 1)
    gracze[i] += talia[e]
    del talia[e]
    n = len(talia)

while gierka == 1:
    p = 'a'

    if g == 2:
        gracze[2] = -1
        gracze[3] = -1
        n = len(talia)

        if gracze[3] < 16:
            e = random.randint(0, n - 1)
            gracze[3] += talia[e]
            del talia[e]
            n = len(talia)

        print("Wynik gracza pierwszego:", gracze[0], " Wynik gracza drugiego:", gracze[1], "Komputer", gracze[3])

        for i in range(g):
            if wynik[i][2] == 'Komputer':
                if gracze[i] < 16:
                    e = random.randint(0, n - 1)
                    gracze[i] += talia[e]
                    del talia[e]
                    n = len(talia)
                else:
                    wynik[i][3] = 'n'
                continue
            if wynik[i][3] != 'n':
                print(wynik[i][1], "Gramy dalej? [t/n]: ")
                p = input()
                if p == 'n':
                    wynik[i][3] = 'n'
                elif wynik[i][3] != 'n':
                    a = random.randint(0, n - 1)
                    gracze[i] += talia[a]
                    del talia[a]
                    n = len(talia)

            czy_gramy_dalej = 1
            for i in range(g):
                if wynik[i][3] == "t":
                    czy_gramy_dalej = 1
                    break
                else:
                    czy_gramy_dalej = 0

            if czy_gramy_dalej != 1:
                gierka = 0
                break

    if g == 3:
        gracze[3] = -1
        n = len(talia)
        if gracze[3] < 16:
            e = random.randint(0, n - 1)
            gracze[3] += talia[e]
            del talia[e]
            n = len(talia)

        print("Wynik gracza pierwszego:", gracze[0], " Wynik gracza drugiego:", gracze[1],
              " Wynik gracza trzeciego:",gracze[2], "Komputer: ", gracze[3])

        for i in range(g):
            if wynik[i][2] == 'komputer':
                if gracze[i] < 16:
                    e = random.randint(0, n - 1)
                    gracze[i] += talia[e]
                    del talia[e]
                    n = len(talia)
                else:
                    wynik[i][3] = 'n'
                continue
            if wynik[i][3] != 'n':
                print(wynik[i][1], "Gramy dalej? [t/n]: ")
                p = input()
                if p == 'n':
                    wynik[i][3] = 'n'
                elif wynik[i][3] != 'n':
                    a = random.randint(0, n - 1)
                    gracze[i] += talia[a]
                    del talia[a]
                    n = len(talia)

            czy_gramy_dalej = 1
            for i in range(g):
                if wynik[i][3] == "t":
                    czy_gramy_dalej = 1
                    break
                else:
                    czy_gramy_dalej = 0

            if czy_gramy_dalej != 1:
                gierka = 0
                break

if gracze[0] > 21:
    gracze[0] = 0
if gracze[1] > 21:
    gracze[1] = 0
if gracze[2] > 21:
    gracze[2] = 0
if gracze[3] > 21:
    gracze[3] = 0

komunikat = 'Gre wygrywa...'
czy_bank = True

for i in range(g):
    if gracze[i] > gracze[3]:
        print(komunikat, wynik[i][1])
        czy_bank = False

if czy_bank and gracze[4] != 0:
    print("Gre wygral bank")

if gracze[0] <= 0 and gracze[1] <= 0 and gracze[2] <= 0 and gracze[3] <= 0 and gracze[4] <= 0:
    print("Nikt nie wygral")
