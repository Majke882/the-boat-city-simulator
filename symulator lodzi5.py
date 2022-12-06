# symulator Łodzi - wyprawa po przedmiesciach łodzi podczas ktorej spotykasz mityczne stwory z ktorymi mozesz walczyc, wybierac co zrobisz rozmawiac 

from random import randint


print('Wybierz plec: m - chlopak, k - dziewczyna')
plec = str(input())
while plec != 'k' or 'm':
    if plec == 'k':
        break
    elif plec == 'm':
        break
    plec = str(input())
    print('Wybierz plec: m - chlopak, k - dziewczyna', plec)


print('wybierz nazwe swojego podroznika: ')
imie = str(input())
imie = randint(1,7)
nazwy_m = ['Sebastian', 'Antoni', 'Jan','Jakub','Aleksander','Franciszek']
nazwy_k = ['Hanna', 'Zofia','Julia','Maja','Zuzanna','Honorata']

rand = randint(0,6)

if plec == 'k':
    los = nazwy_k[rand]
    print('gratulacje twoje imie to: ',los,'(przeciez sama nie wybieralas swojego imienia - podziekuj rodzicom)')
elif plec == 'm':
    los2 = nazwy_m[rand]
    print('Gratulacje twoje imie to: ',los2,'(przeciez sam nie wybierales swojego imienia - podziekuj rodzicom)')

print('Witaj na przedmiesciach Lodzi, na które zdarzyło ci się trafic przez przenikanie sie swiatow, zwane koniunkcja sfer.')
print('Twoim zadaniem w tej ciemnej i nieprzyjaznej krainie jest przezyc dopoki efekty koniunkcji sie nie ustatkuja','\n','Podroz przez rozne swiaty bardzo cie zmeczyla - ruszasz przed siebie zeby znalezc cos do jedzenia')
print('W twoja strone zmierza 𝐬𝐳𝐥𝐚𝐜𝐡𝐞𝐭𝐧𝐲 czlowiek dosiadajacy dzika: czy chcesz go zatrzymac','\n','i poprosic o jedzenie i informacje?')
szlachcic = str(input('chcesz?'))

while szlachcic != 'nie' and 'tak':
    szlachcic = str(input('chcesz?'))
    if szlachcic == 'nie':
        print('Boisz sie czlowieka z dzikiem - wolisz go nie zatrzymywac')
        break
    elif szlachcic == 'tak' and 'jeszcze jak':
        print('na pewno?')
        szlachcic = str(input('chcesz?'))
        if szlachcic == 'tak' and 'jak najbardziej':
            print('probujesz zatrzymac szlachcica galopujacego w twoja strone')
            break
        elif szlachcic == 'nie':
            print('latwo zmieniasz zdanie...')
            break
print('uwu')

#walka opiera sie na atakach, ktore mozesz wyprowadzic - przeciwnik rowniez takie posiada, oboje macie po 100hp. Walka toczy się dopoki ktos nie bedzie mial 0hp.

b_atk = 3
b_atkspc = 9

def walka():
    hp_wrog = 100
    hp_bohater = 100
    A1 = b_atk
    A2 = b_atkspc
    y = hp_wrog - b_atk
    z = hp_wrog - b_atkspc
    while hp_wrog > 0 and hp_bohater > 0:
        print('wybierz atk','\n','A1 to zwykly atak','\n','A2 to atak specjalny')
        x = input()
        if x == 'A1':
            print(y)
            hp_wrog = y
        elif x == 'A2':
            print(y)
            hp_wrog = y
        print('jeszcze raz')

print(walka())

print('twoj powrot do domu zaczyna sie przedluzac, gubisz sie, a swiat dookola zaczyna powoli zapadac w sen.','\n','wyglada na to, ze nie masz wyjscia i musisz zrobic to samo.','\n','szukasz miejsca w ktorym ktos moglby cie przyjac i widzisz chate w ktorej pala sie swiatla')
wej = input('chcesz tam wejsc?')
if wej == 'tak':
    print('kierujesz swoje kroki ku dziwnej chacie')
elif wej == 'nie':
    print('zdrowy rozsadek podpowiada ci, ze smierc z powodu zamarzniecia lub dzikow jest gorsza, dlatego ogladasz okolice domu w poszukiwaniu miejsca spoczynku bez wiedzy domownikow chaty','\n', 'zauwazasz obore obok domu, ktora wydaje sie byc pusta ale dosc przytulna - decydujesz sie tam spedzic noc')
    print('noc przebiega spokojnie, jednak glod oslabia cie, dlatego twoje zdrowie na tym cierpi')
    hp_bohater = 90
else:
    print('widocznie ciemnosc zabrala ci mozliwosc decydowania w kwestii wyboru logicznego. Nic sie nie stalo, sprobuj jeszcze raz.')
    wej = input('chcesz tam wejsc?')    
    if wej == 'tak':
        print('kierujesz swoje kroki ku dziwnej chacie')
        print('mieszkancy cieplo cie witaja, czestuja chlebem i sola po czym zmeczony kladziesz sie spac')
    elif wej == 'nie':
        print('zdrowy rozsadek podpowiada ci, ze smierc z powodu zamarzniecia lub dzikow jest gorsza, dlatego ogladasz okolice domu w poszukiwaniu miejsca spoczynku bez wiedzy domownikow chaty','\n', 'zauwazasz obore obok domu, ktora wydaje sie byc pusta ale dosc przytulna - decydujesz sie tam spedzic noc')
        print('noc przebiega spokojnie, jednak glod oslabia cie, dlatego twoje zdrowie na tym cierpi')
        hp_bohater = 90

